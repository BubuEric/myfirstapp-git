from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin


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
            "id":"inputPassword",
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

