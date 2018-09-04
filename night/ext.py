from night.views import blue
from flask_bootstrap import Bootstrap

def init_ext(app):
    app.register_blueprint(blueprint=blue)
    Bootstrap(app)