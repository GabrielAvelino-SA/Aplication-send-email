from flask import Flask, request, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@10.5.0.4:5432/northwind"

# login_manager = LoginManager(app)
# db = SQLAlchemy(app)

from app.controllers import default
