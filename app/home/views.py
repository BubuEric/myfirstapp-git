from . import home
from flask import render_template, redirect, url_for
from app.models import Tag, Tagname, Tagurl

@home.route('/')
def index():
    data_tag = Tag.query.all()
    data_tagname = Tagname.query.all()
    data_tagurl = Tagurl.query.all()
    return render_template('home/home.html',data_tag=data_tag, data_tagname=data_tagname,data_tagurl=data_tagurl)


@home.route('/fuli/')
def fuli():
    return render_template('home/fuli.html')
