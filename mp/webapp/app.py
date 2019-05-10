#!/usr/bin/env python3
import os
from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


def getData():
    time = datetime.now().strftime("%H:%M:%S")
    temp = round(25, 1)
    return time, temp

# main route
@app.route("/")
def index():
    time, temp = getData()
    templateData = {
        'time': time,
        'temp': temp
    }
    return render_template('index.html', **templateData)

@app.route("/booklist")
def booklist():
    # time, temp = getData()
    books = [{
        "title": "Lord of The Rings",
        "author": "JRR Tolkien"
    },
    {
        "title": "Harry Potter",
        "author": "JR Rowling"
    }]
    return render_template('booklist.html', books=books)


if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)
