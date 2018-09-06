from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:xu1122..@127.0.0.1:3306/myapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
db = SQLAlchemy(app)
app.debug = True

from app.home import home as home_Blueprint
from app.admin import admin as admin_Blueprint

app.register_blueprint(home_Blueprint)
app.register_blueprint(admin_Blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
