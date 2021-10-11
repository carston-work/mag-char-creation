from flask import Flask
from app.extensions import *
from app.mystuff import *


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = f'{secret_key}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pgusername}:{pgpass}@localhost:5432/mag-character-creator'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True    

    init_extensions(app)

    from app.main.views import home, main
    from app.auth.views import auth
    app.add_url_rule('/', view_func=home)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app