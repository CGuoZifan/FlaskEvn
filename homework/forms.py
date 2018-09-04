from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username=StringField(label='用户名',validators=[DataRequired(message='这个字段不能为空')])
    password=PasswordField(label='密码',validators=[DataRequired(message='这个字段不能为空')])
    submit=SubmitField(label='提交')