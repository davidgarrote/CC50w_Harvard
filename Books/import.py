# Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books.
# Each one has an ISBN number, a title, an author, and a publication year. 
# In a Python file called import.py separate from your web application, write a program that will take the books and import them into your PostgreSQL database.
# You will first need to decide what table(s) to create, what columns those tables should have, and how they should relate to one another.
# Run this program by running python3 import.py to import the books into your database, and submit this program with the rest of your project code

import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader: # loop gives each column a name
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year) LIMIT 5000",
                    {"isbn": isbn, "title": title,"author": author, "year": year}) # substitute values from CSV line into SQL command, as per this dict
        print(f"Added book with ISBN {isbn}, title {title}, author {author} and year {year}.")
        db.commit() # transactions are assumed, so close the transaction finished

if __name__ == "__main__":
    main()