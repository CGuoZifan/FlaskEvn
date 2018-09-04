from flask import Blueprint, request, render_template, redirect, url_for, jsonify

from app.form import ProductForm
from .models import *
blue=Blueprint('blue',__name__)
# 首页
@blue.route('/index/')
def index():
        # 获取cookie
        username=request.cookies.get('username','游客')
        return render_template('base.html',username=username)
# 登陆页面,显示列表
@blue.route('/login/',methods=['GET','POST'])
def login():
        if request.method=='GET':
                return render_template('login.html')
        elif request.method=='POST':
                username=request.form.get('username','游客')
                # 设置cookie
                respon=redirect(url_for('blue.index'))
                respon.set_cookie('username',username)
                students = Student.query.all()
                return render_template('index.html',**locals())

# 退出
@blue.route('/quit/')
def quit():
        # 删除cookie
        respon=redirect(url_for('blue.index'))
        respon.delete_cookie('username')
        return respon
#wtf
@blue.route('/p1',methods=['GET','POST'])
def product_view():
        name=None  #用来存储提交来的表单数据
        form=ProductForm()  #表单的实例化对象
        # vallidate只有表单被提交了,它才会
        if form.validate_on_submit():  #表单提交后进行验证,如果验证通过返回True
                name=form.proname.data  #data指的是获取表单的数据，并赋值给name变量
                form.proname.data=''  #清空表单数据
        return render_template('product.html',name=name,form=form)

@blue.route('/fruit')
def fruit():
        return jsonify({'name':'草莓','price':19.9,'color':'red'})















