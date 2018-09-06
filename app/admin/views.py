from . import admin
from flask import render_template, redirect, url_for, flash, session, request, abort
from app.admin.forms import LoginForm
from app.models import Admin
from functools import wraps
from app import db, app


# csrf.init_app()


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


# 导航管理
@admin.route("/tag/add/", methods=["GET"])
@admin_login_req
def tag_add():
    return render_template('admin/tag_add.html')


# 导航列表
@admin.route("/tag/list/", methods=["GET"])
@admin_login_req
def tag_list():
    return render_template('admin/tag_list.html')