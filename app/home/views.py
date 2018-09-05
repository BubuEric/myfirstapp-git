from . import home
from flask import render_template, redirect, url_for


@home.route('/')
def index():
    return render_template('home/home.html')


@home.route('/fuli/')
def fuli():
    return render_template('home/fuli.html')
