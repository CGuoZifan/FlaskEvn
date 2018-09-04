from flask import Flask
from night.ext import init_ext

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='aedfawef'
    init_ext(app)
    return app