from datetime import datetime
from app import db

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/myapp"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
# db = SQLAlchemy(app)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员账号
    pwd = db.Column(db.String(100))  # 管理员密码
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)



# 一级标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    num = db.Column(db.BigInteger)  # 序号
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    tagnames = db.relationship("Tagname", backref='tag')  #二级标签外键关联


    def __repr__(self):
        return "<Tag %r>" % self.name


# 二级标签
class Tagname(db.Model):
    __tablename__ = "tagname"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属一级标签
    tagurls = db.relationship("Tagurl", backref='tagname')  # 二级标签外键关联

    def __repr__(self):
        return "<Tagname %r>" % self.name


# 网站网址
class Tagurl(db.Model):
    __tablename__ = "tagurl"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 网站名称
    url = db.Column(db.String(100), unique=True)  # 网址
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    tagname_id = db.Column(db.Integer, db.ForeignKey('tagname.id'))  # 所属二级标签

    def __repr__(self):
        return "<Tagurl %r>" % self.name





# 博客
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    content = db.Column(db.Text)  # 内容
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "Blog %r" % self.title

if __name__ == '__main__':
    db.create_all()
'''
if __name__ == '__main__':
    db.create_all()
   
    from werkzeug.security import generate_password_hash

    admin = Admin(
        name='eric',
        pwd=generate_password_hash('xu1122..'),

    )
    db.session.add(admin)
    db.session.commit()
'''
