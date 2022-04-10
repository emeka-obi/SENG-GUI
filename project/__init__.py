from flask import Flask
import flask_login
from flask_sqlalchemy import SQLAlchemy
from utils.config import Config
import os
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # database configurations, and secret_key setup
    app.config['SECRET_KEY'] = os.urandom(12)
    app.config['FLASK_ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config.from_object(Config)

    db.init_app(app)
    # To handle sessions
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))



    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app