from flask import Flask

# Loads the views file
from app import views


# importing locally
from instance.config import app_config

# initializing sql-alchemy
db = SQLAlchemy()

def wsgi_app(self, environ, start_response):
    app.wsgi_app = MyMiddleware(app.wsgi_app)
    response = self.handle_exception(e)

    return self.wsgi_app

def __call__(self, environ, start_response):

    return self.wsgi_app(environ, start_response)

def current_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py') #loading config file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app