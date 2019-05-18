#!/usr/bin/env python3
import os, requests, json
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, HiddenField

app = Flask(__name__)
bootstrap = Bootstrap(app)


class AddBookForm(Form):
    book_ISBN = StringField('ISBN')
    book_title = StringField('Title')
    book_author = StringField('Author')


"""
class EditBookForm(Form):
    bookID = HiddenField('0')


class DeleteBookForm(Form):
    bookID = HiddenField('0')
"""

# main route
@app.route("/")
def index():
    return render_template('index.html')

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
    
    if request.method == 'POST':
        ISBN = addBookForm.book_ISBN.data
        title = addBookForm.book_title.data
        author = addBookForm.book_author.data
        requests.post("http://127.0.0.1:5001/book", None,
            {"ISBN": ISBN, "Title": title, "Author": author})
    
    response = requests.get("http://127.0.0.1:5001/book")
    books = json.loads(response.text)
    return render_template('booklist.html', books=books, addBookForm=addBookForm)


if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)
