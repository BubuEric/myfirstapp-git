from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag, Tagname


class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            "id": "inputPassword",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )

    def validate_account(self, field):
        account = field.data
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            raise ValidationError("账号不存在！")


# 添加一级标签
class TagForm(FlaskForm):
    name = StringField(
        label='导航名称',
        validators=[
            DataRequired('请输入导航名称'),
        ],
        description='导航名称',
        render_kw={
            'class': "form-control",
            'id': "InputName",
            'placeholder': "请输入导航名称！"
        }
    )

    num = IntegerField(
        label='序号',
        validators=[
            DataRequired('请输入序号'),
        ],
        description='序号',
        render_kw={
            'class': "form-control",
            'id': "InputNum",
            'placeholder': "请输入序号！"
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': "btn btn-default pull-right"
        }
    )


# 添加二级分类
class TagnameForm(FlaskForm):
    name = StringField(
        label='分类名称',
        validators=[
            DataRequired('请输入分类名称'),
        ],
        description='分类名称',
        render_kw={
            'class': "form-control",
            'id': "InputName",
            'placeholder': "请输入分类名称！"
        }
    )

    tag_id = SelectField(
        label='所属导航',
        validators=[
            DataRequired("请选择所属导航！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Tag.query.all()],
        description="标签",
        render_kw={
            "class": "form-control",
        }

    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': "btn btn-default pull-right"
        }
    )


# 添加网站
class TagurlForm(FlaskForm):
    name = StringField(
        label='网站名称',
        validators=[
            DataRequired('请输入网站名称'),
        ],
        description='网站名称',
        render_kw={
            'class': "form-control",
            'id': "InputName",
            'placeholder': "请输入网站名称！"
        }
    )

    url = StringField(
        label='网址',
        validators=[
            DataRequired('请输入网址'),
        ],
        description='网址',
        render_kw={
            'class': "form-control",
            'id': "InputName",
            'placeholder': "请输入网址！"
        }
    )

    tagname_id = SelectField(
        label='所属分类',
        validators=[
            DataRequired("请选择所属分类！")
        ],
        coerce=int,
        choices=[(v.id, v.name) for v in Tagname.query.all()],
        description="分类",
        render_kw={
            "class": "form-control",
        }

    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': "btn btn-default pull-right"
        }
    )