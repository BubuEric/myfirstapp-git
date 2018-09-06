from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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



# 添加导航
class TagForm(FlaskForm):
    name = StringField(
        label='网站名称',
        validators=[
            DataRequired('请输入网站名称'),
        ],
        description='网站名称',
        render_kw={
            'class': "form-control",
            'id': "input_name",
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
            'id': "input_name",
            'placeholder': "请输入标签网址！"
        }
    )

    submit = SubmitField(
        '编辑',
        render_kw={
            'class': "btn btn-primary"
        }
    )

