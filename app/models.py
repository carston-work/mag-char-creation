from app import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    characters = db.relationship("Character", backref='creator', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def get_id(self):
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Character(db.Model):
    
    __tablename__ = "characters"

    character_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    concept = db.Column(db.String(40), nullable=False)
    preferences = db.Column(db.Integer)

    def __init__(self, creator_id, name, concept, preferences):
        self.creator_id = creator_id
        self.name = name
        self.concept = concept
        self.preferences = preferences