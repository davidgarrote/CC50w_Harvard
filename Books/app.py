import os

from flask import Flask, session, render_template, redirect, request, session, flash, g, request, url_for, jsonify
from functools import wraps
from flask_session import Session
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash
from contextlib import contextmanager
import requests



# app = Flask(__name__) # to make the app run without any
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def trim_author(self):
        author_len = len(self.author)
        if author_len > 2:
            del self.author[2:]
        self.author = ", ".join(self.author)
        if author_len > 2:
            self.author = self.author + " and more"


class Rev:
    def __init__(self, username, text, review_id, rating):
        self.username = username
        self.text = text
        self.review = review_id
        self.rating = rating


@app.route("/")
def index():
    return render_template("search.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()
    if request.method == "POST": 
        
        # Define variables from user input
        userlogin = request.form.get("username")
        pwlogin = request.form.get("password")

        # Check username and user were submitted
        if not userlogin or not pwlogin:
            flash("Please submit username and password")
            return redirect("/login")

        else:
            # Query database for the user information
            rows = db.execute("SELECT * FROM users WHERE username = :username",
            {"username": userlogin}).fetchone()

        # If rows returns None prompt the user with an error
        if rows == None:
            flash("Please input a valid username and password")
            return redirect ("/login")

        # Check if password matches
        if check_password_hash(rows.hash, pwlogin) == False:
            flash("Password doesn't match")
            return redirect ("/login")
        
        else:
            # Remember which user has logged in
            
            
            #Remember the name from the user logged in
            session["logged_in"] = True
            session["user_id"] = rows.id
            session["user_name"] = rows.username

            # Redirect user to home page
            return redirect("/")
            flash("Welcome back!")
    
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":    

        #Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username")
            return redirect("/register")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password")
            
        # Ensure password was correcly repeated
        elif not request.form.get("repeat_password"):
            flash("Must repeat password")

        #Ensure passwords match
        username = request.form.get("username")
        if request.form.get("password") != request.form.get("repeat_password"):
            flash("Password don't match")

        # Hash password and create new user

        else:
            hashed_pw = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES (:name, :hash)",
                    {"name": username, "hash": hashed_pw})
            db.commit()
            flash("Register successful")
            return redirect(url_for('register'), "303")

    else:
        if session.get('logged_in'):
            flash("You are already registered!")
        else:
            return render_template("register.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if not session.get('logged_in'):
        return("You must be logged in to search for books")

    else:
        if request.method == "POST":
            
            book_search = request.form.get("book_search")
            book_search = f"%{book_search}%".lower()
            results = db.execute("SELECT title,author,year,isbn FROM books WHERE LOWER(title) LIKE :title OR LOWER(author) LIKE :author OR year LIKE :isbn",
            {"title": book_search, "author": book_search, "isbn": book_search}).fetchall()
            books = []
            for title, author, year, isbn in results:
                new_book = Book(title, author, year, isbn)
                books.append(new_book)
            if len(books) < 1:
                flash("No results found!")
            return render_template("search.html", books=books)

        else:
            return render_template("search.html")

@app.route("/book/<string:book_id>", methods=["GET"])
def book(book_id):
    if not session.get('logged_in'):
        return("You must be logged in to search for books")
    else:
        if request.method == "GET":

            results = db.execute("SELECT title,author,year,isbn FROM books WHERE isbn = :isbn",
            { "isbn": book_id}).fetchall()
            books = []
            for title, author, year, isbn in results:
                new_book = Book(title, author, year, isbn)
                books.append(new_book)
            # Show the reviews
            revi = db.execute("SELECT username, text, review_id, rating FROM reviews LEFT JOIN users ON reviews.user_id = users.id WHERE book_id = :book_id", {"book_id": book_id})
            reviews = []
            for username, text, review_id, rating in revi:
                new_reviews = Rev(username, text, review_id, rating)
                reviews.append(new_reviews)
            
            key = "caYtzAroyZw3ev8m9gBD9Q"

            res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": book_id})
            data = res.json()
            rating = float(data['books'][0]['average_rating'])
            count = int(data['books'][0]['reviews_count'])


            return render_template("book.html", books=books, reviews=reviews, res=res, count=count, rating=rating)

@app.route("/reviews", methods=["POST"])
def reviews():
    if not session.get('logged_in'):
        return("You must be logged in to search for books")
    else:
        if request.method == "POST":
            #Extract the review from the forms
            rating = request.form.get("rating")
            text = request.form.get("text")
            book_id = request.form.get("book_id")

            #Save the review
            db.execute("INSERT INTO reviews (user_id, book_id, rating, text) VALUES (:user_id, :book_id, :rating, :text)", {"user_id": session["user_id"], "book_id": book_id, "rating": rating, "text": text})
            db.commit()

            flash("Thank you for submitting your review!")

            
            return redirect(url_for('book', book_id=book_id), "303")

@app.route("/api/<string:isbn>", methods=["GET"])
def api(isbn):
    if request.method == "GET":
        databook = db.execute("SELECT title, author, year, isbn from books where isbn = :isbn", {"isbn": isbn}).fetchone()
        if databook is None:
            return jsonify(
            {
                "error_code": 404,
                "error_message": "Not Found"
            }
        ), 404
        else:
            key = "caYtzAroyZw3ev8m9gBD9Q"
            res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
            data = res.json()
            rating = float(data['books'][0]['average_rating'])
            count = int(data['books'][0]['reviews_count'])

            result = {
                "title": databook.title, "author": databook.author, "year": int(databook.year), "isbn": databook.isbn, "review_count": count, "average_score": rating
                }
            return jsonify(result)
