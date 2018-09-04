from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    # 文本                     DataRequired，必填，不能为空
    proname=StringField(label="产品名称",validators=[DataRequired(message="这个字段不能为空")])#message提示信息
    # 提交按钮
    submit=SubmitField(label="点击提交")
