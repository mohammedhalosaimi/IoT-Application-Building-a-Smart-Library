#!/usr/bin/env python3
import os
from flask import Flask, request, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from controller import RouteController
from login_controller import login_controller

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = "lFgz7p1PZR6I63He3VvxtCmWdCPf"
app.add_url_rule('/', 'index', lambda: RouteController.index())
app.add_url_rule('/booklist', 'booklist', lambda: RouteController.booklist(), methods=['GET', 'POST'])
app.add_url_rule('/datavis', 'datavis', lambda: RouteController.data_vis())
app.add_url_rule('/login', 'login', lambda: RouteController.login_post(), methods=['POST', 'GET'])
app.add_url_rule('/logout', 'logout', lambda: RouteController.logout())
app.add_url_rule('/delete', 'delete', lambda: RouteController.removeBook(), methods=['POST'])
app.add_url_rule('/update', 'update', lambda: RouteController.updateBook(), methods=['POST'])


if __name__ == "__main__":
    host = os.popen('hostname -I').read()
    app.run(host=host, port=80, debug=False)


