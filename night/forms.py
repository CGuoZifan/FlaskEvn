from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username=StringField(label="用户名:",validators=[DataRequired(message="必须填写用户名")])
    password=PasswordField(label="密码",validators=[DataRequired(message="必须填写密码")])
    sub=SubmitField(label="登陆")