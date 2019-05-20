#!/usr/bin/env python3
import os, requests, json
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, HiddenField

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = "lFgz7p1PZR6I63He3VvxtCmWdCPf"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "abc123"


class AddBookForm(Form):
    book_ISBN = StringField('ISBN')
    book_title = StringField('Title')
    book_author = StringField('Author')

# main route
@app.route("/")
def index():
    if "logged_in" in session:
        logged_in = True
    else:
        logged_in = False
    return render_template('index.html', logged_in=logged_in)

@app.route("/delete", methods=['POST'])
def removeBook():
    id = request.form.get("id")
    requests.delete("http://127.0.0.1:5001/book/"+id)
    return redirect("/booklist")

@app.route("/update", methods=['POST'])
def updateBook():
    id = request.form.get("id")
    newISBN = request.form.get("newName")
    newTitle = request.form.get("newTitle")
    newAuthor = request.form.get("newAuthor")
    requests.put("http://127.0.0.1:5001/book/"+id,
        json={"ISBN": newISBN, "Title": newTitle, "Author": newAuthor})
    return redirect("/booklist")

@app.route("/booklist", methods=['GET', 'POST'])
def booklist():
    addBookForm = AddBookForm(request.form)
    if 'logged_in' in session:
            if request.method == 'POST':
                ISBN = addBookForm.book_ISBN.data
                title = addBookForm.book_title.data
                author = addBookForm.book_author.data
                requests.post("http://127.0.0.1:5001/book", None,
                              {"ISBN": ISBN,
                               "Title": title,
                               "Author": author})
        
            if request.method == 'GET':
                response = requests.get("http://127.0.0.1:5001/book")
                books = json.loads(response.text)
                return render_template('booklist.html',
                                       books=books,
                                       addBookForm=addBookForm)
    else:
        return redirect('/')

@app.route('/login', methods=['POST', 'GET'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if(username == ADMIN_USERNAME and password == ADMIN_PASSWORD):
            session["logged_in"] = True
            return redirect('/')
        else:
            return redirect('/')
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
