from app import app
# from app.models import tables
from flask import Flask, request, render_template,url_for, redirect

@app.route("/")
def index():
    return ('API 0.0.1')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")
@app.route("/register", methods=['GET', 'POST'])
def reguster():
    return render_template('register.html')