# Project 1

Web Programming with Python and JavaScript

My webpage for Project 1 is called Winbooks, and it allows users to find book by Author, date, title or ISBN.
The users must be registered in order to access to the webpage.

Once logged in, users can search for a book, leave a review and see reviews posted by the rest of the users.

If desired, users can take advantage of our built-in API which provides machine-readable information about the books in our database, if the book is not available it will return an error.

What is included in the files?

app.py -> Main application containing the app functionalities and imported packages

Templates -> 
	Layout, that is extended to the rest of the html pages
	Register: username, password and repeat password. Shows error if any of the fields is not completed, if passwords don't match and it the username has been already taken by a different user.
	Login: simple login with 2 input fields, if login successful it redirects to the search section
	search: contains the search page
	book: included has the /book /reviews and takes the information from Goodreads to show a fully functional and detailed book page.
	api: simple api page that loads the json objects created with the jsonfy function

static->
	css->
		style.css: contains the CSS applied to all the html pages
		logo: webpage logo

import.py -> python file that takes the comma separated list of books and inputs it into the Heroku database


		