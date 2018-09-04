from flask import render_template, Blueprint, session, redirect, url_for, flash
from homework.forms import UserForm
from flask.json import jsonify
blue=Blueprint("blue",__name__)

@blue.route('/login' ,methods=['GET','POST'])
def login_view():
    userForm=UserForm()
    if userForm.validate_on_submit():
        username=userForm.data.get("username")
        password=userForm.data.get("password")
        if username=="tom" and password=="123456":
            return redirect(url_for("blue.success_view"))
        else:
            flash("用户名或密码不正确")
    return render_template('login.html',userForm=userForm)

@blue.route("/success")
def success_view():
    return render_template("success.html")

@blue.route('/fruit/')
def fruit():
    return jsonify({'name':['banana','apple','watermelon']})

@blue.route('/sport/')
def sport():
    return jsonify({'name':['football','basktable','pingpang']})

@blue.route('/things/')
def things_view():
    return render_template("things.html")