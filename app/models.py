from datetime import datetime
from app import db


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


# 网站网址
class TagC(db.Model):
    __tablename__ = "tagc"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 网站名称
    url = db.Column(db.String(100), unique=True)  # 网站名称
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间


    def __repr__(self):
        return "<TagC %r>" % self.name


# 二级标签
class TagB(db.Model):
    __tablename__ = "tagb"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称

    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间


    def __repr__(self):
        return "<TagB %r>" % self.name


# 一级标签
class TagA(db.Model):
    __tablename__ = "taga"
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    num = db.Column(db.INTEGER, primary_key=True)  # 序号
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间


    def __repr__(self):
        return "<TagA %r>" % self.name


# 博客
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.INTEGER, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    content = db.Column(db.Text)  # 内容
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间

    def __repr__(self):
        return "Blog %r" % self.title


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
