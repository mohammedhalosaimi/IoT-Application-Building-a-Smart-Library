#!/usr/bin/env python3
import os, requests, json
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, HiddenField, validators
from login_controller import login_controller

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = "lFgz7p1PZR6I63He3VvxtCmWdCPf"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "abc123"
# The base IP address of the API will be local machine IP at port 5001
API_IP = "http://"+os.popen('hostname -I').read().rstrip()+":5001/"


class AddEditBookForm(Form):
    book_ISBN = StringField('ISBN', [validators.Length(min=1, max=100)])
    book_title = StringField('Title', [validators.Length(min=1, max=100)])
    book_author = StringField('Author', [validators.Length(min=1, max=100)])

# main route
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/delete", methods=['POST'])
def removeBook():
    id = request.form.get("id")
    requests.delete(API_IP + "book/"+id)
    return redirect("/booklist")


@app.route("/update", methods=['POST'])
def updateBook():
    id = request.form.get("id")
    addBookForm = AddEditBookForm(request.form)
    newISBN = addBookForm.book_ISBN.data
    newTitle = addBookForm.book_title.data
    newAuthor = addBookForm.book_author.data
    requests.put(API_IP + "book/"+id,
                 json={"ISBN": newISBN,
                       "Title": newTitle,
                       "Author": newAuthor})
    return redirect("/booklist")


@app.route("/booklist", methods=['GET', 'POST'])
def booklist():
    addBookForm = AddEditBookForm(request.form)
    if 'logged_in' in session:
            if request.method == 'POST':
                if not addBookForm.validate():
                    return redirect(url_for("booklist"))
                ISBN = addBookForm.book_ISBN.data
                title = addBookForm.book_title.data
                author = addBookForm.book_author.data
                requests.post(API_IP + "book", None,
                              {"ISBN": ISBN,
                               "Title": title,
                               "Author": author})
                return redirect(url_for("booklist"))
        
            if request.method == 'GET':
                response = requests.get("http://10.132.105.42:5001/book")
                books = json.loads(response.text)
                return render_template('booklist.html',
                                       books=books,
                                       addBookForm=addBookForm)
    else:
        return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login_post():

    if request.method == 'POST':
        if login_controller.validate_login(request):
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            error = "Invalid login information"
            return render_template("login.html", error=error)
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    if'logged_in' in session:
        session.pop("logged_in", None)
        return redirect('/')
    else:
        return "<h4>You must be logged in to log out<h4>"


if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)
