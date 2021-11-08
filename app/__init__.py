from flask import Flask
from app.extensions import *
from app.mystuff import *

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pgusername}:{pgpass}@localhost:5432/mag-character-creator'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True    

    app.config["RECAPTCHA_PUBLIC_KEY"] = recaptcha_public
    app.config["RECAPTCHA_PRIVATE_KEY"] = recaptcha_private

    init_extensions(app)    

    from app.main.views import home, main
    from app.auth.views import auth
    from app.users.views import users
    from app.characters.views import char
    from app.crews.views import crew
    app.add_url_rule('/', view_func=home)
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(users, url_prefix="/users")
    app.register_blueprint(char, url_prefix="/char")
    app.register_blueprint(crew, url_prefix="/crew")    

    return app