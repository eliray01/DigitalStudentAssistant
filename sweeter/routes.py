from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

from sweeter import db, app

@app.route("/login", methods = ['GET','POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        pass
    else:
        return render_template('login.html')

@app.route("/register", methods = ['GET','POST'])
def register():
    pass

@app.route("/logout", methods = ['GET','POST'])
def logout():
    pass