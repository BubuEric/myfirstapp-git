from . import admin
from flask import render_template, redirect, url_for, flash, session, request, abort, jsonify
from app.admin.forms import LoginForm, TagForm, TagnameForm, TagurlForm
from app.models import Admin, Tag, Tagname, Tagurl
from functools import wraps
from app import db, app
import json
from flask_paginate import Pagination,get_page_parameter


# 登录装饰器
def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@admin.route("/")
@admin_login_req
def index():
    return render_template("admin/index.html")


@admin.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误！", 'err')
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        session["admin_id"] = admin.id
        # adminlog = Adminlog(
        #     admin_id=admin.id,
        #     ip=request.remote_addr,
        # )
        # db.session.add(adminlog)
        # db.session.commit()
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template("admin/login.html", form=form)


# 退出
@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("admin.login"))


# 添加导航
@admin.route("/tag/add/", methods=["GET", "POST"])
@admin_login_req
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["name"]).count()
        if tag == 1:
            flash("名称已经存在！", "err")
            return redirect(url_for('admin.tag_add'))
        tag = Tag.query.filter_by(num=data["num"]).count()
        if tag == 1:
            flash("序号已经存在！", "err")
            return redirect(url_for('admin.tag_add'))
        tag = Tag(
            name=data["name"],
            num=data["num"]
        )
        db.session.add(tag)
        db.session.commit()
        flash("添加标签成功！", "ok")
        redirect(url_for('admin.tag_add'))
    return render_template("admin/tag_add.html", form=form)


# 编辑导航
@admin.route("/tag/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def tag_edit(id=None):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data["name"]).count()
        if tag.name != data["name"] and tag_count == 1:
            flash("导航已经存在！", "err")
            return redirect(url_for('admin.tag_edit', id=id))
        tag_count = Tag.query.filter_by(num=data["num"]).count()
        if tag.num != data["num"] and tag_count == 1:
            flash("顺序序号已经存在！", "err")
            return redirect(url_for('admin.tag_edit', id=id))
        tag.name = data["name"]
        tag.num = data["num"]
        db.session.add(tag)
        db.session.commit()
        flash("修改导航成功！", "ok")
        redirect(url_for('admin.tag_edit', id=id))
    return render_template("admin/tag_edit.html", form=form, tag=tag)


# 导航列表
@admin.route("/tag/list/<int:page>/", methods=["GET"])
@admin_login_req
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/tag_list.html", page_data=page_data)


# 导航删除
@admin.route("/tag/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def tag_del(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    db.session.delete(tag)
    db.session.commit()
    flash("删除导航成功！", "ok")
    return redirect(url_for('admin.tag_list', page=1))


# 添加二级标签
@admin.route("/tagname/add/", methods=["GET", "POST"])
@admin_login_req
def tagname_add():
    form = TagnameForm()
    if form.validate_on_submit():
        data = form.data
        tagname = Tagname.query.filter_by(name=data["name"]).count()
        if tagname == 1:
            flash("名称已经存在！", "err")
            return redirect(url_for('admin.tag_add'))
        tagname = Tagname(
            name=data["name"],
            tag_id=int(data["tag_id"]),
        )
        db.session.add(tagname)
        db.session.commit()
        flash("添加标签成功！", "ok")
        redirect(url_for('admin.tagname_add'))
    return render_template("admin/tagname_add.html", form=form)


# 编辑二级分类
@admin.route("/tagname/edit/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def tagname_edit(id=None):
    form = TagnameForm()
    tagname = Tagname.query.get_or_404(id)
    if request.method == "GET":
        form.tag_id.data = tagname.tag_id
    if form.validate_on_submit():
        data = form.data
        tagname_count = Tag.query.filter_by(name=data["name"]).count()
        if tagname.name != data["name"] and tagname_count == 1:
            flash("分类已经存在！", "err")
            return redirect(url_for('admin.tagname_edit', id=id))
        tagname.name = data["name"]
        tagname.tag_id = data["tag_id"]
        db.session.add(tagname)
        db.session.commit()
        flash("修改分类成功！", "ok")
        redirect(url_for('admin.tagname_edit', id=id))
    return render_template("admin/tagname_edit.html", form=form, tagname=tagname)


# 二级标签列表
@admin.route("/tagname/list/", methods=["GET"])
@admin_login_req
def tagname_list():
    PER_PAGE = 10
    total = Tagname.query.count()
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page-1)*PER_PAGE
    end = start +PER_PAGE
    pagination = Pagination(bs_version=3,page=page,total=total)
    articles = Tagname.query.slice(start,end)
    context ={
        'pagination':pagination,
        'articles':articles
    }
    return render_template("admin/tagname_list.html", **context)


# 分类删除
@admin.route("/tagname/del/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def tagname_del(id=None):
    tagname = Tagname.query.filter_by(id=id).first_or_404()
    db.session.delete(tagname)
    db.session.commit()
    flash("删除分类成功！", "ok")
    return redirect(url_for('admin.tagname_list', page=1))


# 添加网站
@admin.route("/tagurl/add/", methods=["GET", "POST"])
@admin_login_req
def tagurl_add():
    form = TagurlForm()
    if form.validate_on_submit():
        data = form.data
        tagurl = Tagurl.query.filter_by(name=data["name"]).count()
        if tagurl == 1:
            flash("名称已经存在！", "err")
            return redirect(url_for('admin.tagurl_add'))
        tagurl = Tagurl(
            name=data["name"],
            url=data["url"],
            tagname_id=int(data["tagname_id"]),
        )
        db.session.add(tagurl)
        db.session.commit()
        flash("添加网站成功！", "ok")
        redirect(url_for('admin.tagurl_add'))
    return render_template("admin/tagurl_add.html", form=form)


# 编辑网站
@admin.route("/tagurl/list/edit/<int:id>/", methods=["GET"])
@admin_login_req
# @admin_auth
def tagurl_edit(id=None):
    form = TagurlForm()
    tagurl = Tagurl.query.get_or_404(id)
    if request.method == "GET":
        form.tagname_id.data = tagurl.tagname_id
    if form.validate_on_submit():
        data = form.data
        tagurl_count = Tagurl.query.filter_by(name=data["name"]).count()
        if tagurl.name != data["name"] and tagurl_count == 1:
            flash("网站已经存在！", "err")
            return redirect(url_for('admin.tagurl_edit', id=id))
        tagurl.name = data["name"]
        tagurl.url = data["url"]
        tagurl.tagname_id = data["tagname_id"]
        db.session.add(tagurl)
        db.session.commit()
        flash("修改网站成功！", "ok")
        redirect(url_for('admin.tagurl_edit', id=id))
    return render_template("admin/tagurl_edit.html", form=form, tagurl=tagurl)


# # 网站列表
# @admin.route("/tagurl/list/", methods=["GET"])
# @admin_login_req
# def tagurl_list():
#     PER_PAGE = 20
#     total = Tagurl.query.count()
#     page = request.args.get(get_page_parameter(),type=int,default=1)
#     start = (page-1)*PER_PAGE
#     end = start +PER_PAGE
#     pagination = Pagination(bs_version=3,page=page,total=total)
#     articles = Tagurl.query.slice(start,end)
#     context ={
#         'pagination':pagination,
#         'articles':articles
#     }
#     return render_template("admin/tagurl_list.html", **context)


# 网站列表
@admin.route("/tagurl/list/", methods=["GET"])
@admin_login_req
def tagurl_list():
    return render_template('admin/tagurl_list.html')


# 网站数据
@admin.route("/tagurl/data/", methods=["GET", "POST"])
@admin_login_req
def tagurl_data():
    data_tagurl = Tagurl.query.join(Tagname).filter(
        Tagname.id == Tagurl.tagname_id
    )
    info = request.values
    limit = info.get('limit', 10)  # 每页显示的条数
    offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
    row = []
    dicts = {}
    for x in data_tagurl:
        dicts = {'id': x.id, 'name': x.name, 'url': x.url, 'tagname_id': x.tagname.id,'tagname':x.tagname.name}
        row.append(dicts)
    return jsonify({'total':len(row),'rows':row[int(offset):(int(offset)+int(limit))]})


# 网站删除
@admin.route("/tagurl/list/del/<int:id>/", methods=["GET", "POST"])
@admin_login_req
# @admin_auth
def tagurl_del(id=None):
    tagurl = Tagurl.query.filter_by(id=id).first_or_404()
    db.session.delete(tagurl)
    db.session.commit()
    flash("删除分类成功！", "ok")
    return redirect(url_for('admin.tagurl_list'))
