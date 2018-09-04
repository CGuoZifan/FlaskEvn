from flask import Blueprint,session,redirect,url_for,render_template,flash,request
from night.forms import UserForm

blue=Blueprint("blue",__name__)

@blue.route('/login/',methods=['POST','GET'])
def login():
    form=UserForm()
    # 如果确认表单提交了
    if form.validate_on_submit():
        # data指的是获取表单的数据
        username=form.username.data
        password=form.password.data
        if username=='tom'and password=='123456':
            session['username']=username
            return redirect(url_for('blue.go_success'))
        else:
            flash("用户名或密码不正确，请重新输入")
            return redirect(url_for('blue.login'))
    return render_template('login.html',form=form)

@blue.route('/success/')
def go_success():
    return render_template('success.html')