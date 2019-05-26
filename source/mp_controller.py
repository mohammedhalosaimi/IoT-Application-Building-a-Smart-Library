# import os, requests, json
# from datetime import datetime
# from flask import Flask, render_template, request, redirect, session, url_for
# from flask_bootstrap import Bootstrap
# from wtforms import Form, StringField, HiddenField, validators
# from login_controller import login_controller

# The base IP address of the API will be local machine IP at port 5001
# For use at RMIT
# API_IP = "http://"+os.popen('hostname -I').read().rstrip()+":5001/"
# For use at home
# API_IP = "http://127.0.0.1:5001/"

class RouteController:
    @staticmethod
    def index():
        """
            The Index Route
            Parameters:
            Returns: The index.html rendered template
        """
        #return render_template('index.html')

    @staticmethod
    def removeBook():
        """
            The remove book route
            Parameters: Book ID (Gotten through the form)
            Returns: Redirects to the booklist
        """
        #id = request.form.get("id")
        #requests.delete(API_IP + "book/"+id)
        #return redirect("/booklist")
    
    @staticmethod
    def updateBook():
        """
            The Update Book Route.
            Parameters: AddBookForm
            Returns: Redirects to the booklist
        """
        #id = request.form.get("id")
        #addBookForm = AddEditBookForm(request.form)
        #newISBN = addBookForm.book_ISBN.data
        #newTitle = addBookForm.book_title.data
        #newAuthor = addBookForm.book_author.data
        #requests.put(API_IP + "book/"+id,
                     #json={"ISBN": newISBN,
                           #"Title": newTitle,
                           #"Author": newAuthor})
        #return redirect("/booklist")

    @staticmethod
    def booklist():
        """
            The book list route
            Parameters: (GET) Returns a book list. (POST) Inserts a book
            Returns: the book_list template populaed by the books in the system.
        """
        # #addBookForm = AddEditBookForm(request.form)
        # #if 'logged_in' in session:
        #        # if request.method == 'POST':
        #            # if not addBookForm.validate():
        #                 return redirect(url_for("booklist"))
        #             ISBN = addBookForm.book_ISBN.data
        #             title = addBookForm.book_title.data
        #             author = addBookForm.book_author.data
        #             requests.post(API_IP + "book", None,
        #                           {"ISBN": ISBN,
        #                            "Title": title,
        #                            "Author": author})
        #             return redirect(url_for("booklist"))
        
        #         if request.method == 'GET':
        #             response = requests.get(API_IP+"book")
        #             books = json.loads(response.text)
        #             return render_template('booklist.html',
        #                                    books=books,
        #                                    addBookForm=addBookForm)
        # else:
        #     return redirect('/')
    

    @staticmethod
    def login_post():
        """
            The Login route
            Parameters: (GET) Returns the login form. (POST) attempts to login
            Returns: successful login or the login template with error
        """
        # if request.method == 'POST':
        #     if login_controller.validate_login(request):
        #         session["logged_in"] = True
        #         return redirect(url_for("index"))
        #     else:
        #         error = "Invalid login information:"
        #         return render_template("login.html", error=error)
        # if request.method == 'GET':
        #     return render_template('login.html')
    

    @staticmethod
    def data_vis():
        """
            The data visualisation route
            Parameters: 
            Returns: the data vis template links to the google studio
        """
        # if 'logged_in' in session:
        #     return render_template("data_vis.html")
        # else:
        #     return redirect(url_for("index"))
    

    @staticmethod
    def logout():
        """
            The logout route
            Parameters:
            Returns: If logged in, will log the user out
        """
        # if'logged_in' in session:
        #     session.pop("logged_in", None)
        #     return redirect('/')
        # else:
        #     return "<h4>You must be logged in to log out<h4>"

# class AddEditBookForm(Form):
#     book_ISBN = StringField('ISBN', [validators.Length(min=1, max=100)])
#     book_title = StringField('Title', [validators.Length(min=1, max=100)])
#     book_author = StringField('Author', [validators.Length(min=1, max=100)])
    