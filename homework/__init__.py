from flask import Flask
from flask_session import Session
from app.models import db
from app.views import blue


def create_user():
    app=Flask(__name__,static_folder=app) #指向的静态资源目录名，可以不加

    # 设置密钥
    app.config['SECRET_KEY']='df5asd14f5s4sdf13s'
    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    # 设置cookie中存储的key
    app.config['SESSION_COOKIE_NAME']='yy'
    # 设置超时时间
    app.config['PERMANENT_SESSION_LIFETIME']=30
    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite://sqlite3.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # 初始化session
    Session(app)
    return app
