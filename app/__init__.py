from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.mystuff import *


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = f'{secret_key}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pgusername}:{pgpass}@localhost:5432/mag-character-creator'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    db.init_app(app)



    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.login_message = "You need to be logged in to access this page."
    login_manager.login_message_category = "danger"

    from app.main.views import home, main
    from app.auth.views import auth
    app.add_url_rule('/', view_func=home)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app