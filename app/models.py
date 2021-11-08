from app import db, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    characters = db.relationship("Character", backref='creator', lazy=True)
    crews = db.relationship("Crew", backref='owner', lazy=True)

    def get_id(self):
        return self.user_id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Character(db.Model):
    
    __tablename__ = "characters"

    character_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    crew_id = db.Column(db.Integer, db.ForeignKey('crews.crew_id'), nullable=True)
    name = db.Column(db.String(30), nullable=False)
    concept = db.Column(db.String(40), nullable=False)
    preferences = db.Column(db.Integer)

    def __init__(self, creator_id, name, concept, preferences):
        self.creator_id = creator_id
        self.name = name
        self.concept = concept
        self.preferences = preferences

    request = db.relationship("Request", uselist=False, backref="character", lazy=True)


class Crew(db.Model):

    __tablename__ = "crews"

    crew_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(40), nullable=False, unique=True)
    seeking = db.Column(db.Boolean, nullable=False)
    preferences = db.Column(db.Integer, nullable = False)

    def __init__(self, owner_id, name, seeking, preferences):
        self.owner_id = owner_id
        self.name = name
        self.seeking = seeking
        self.preferences = preferences
        
    characters = db.relationship("Character", backref="crew", lazy=True)
    requests = db.relationship("Request", backref="crew", lazy=True)

    def __repr__(self):
        owner = self.owner.username
        characters = len(self.characters)
        return f'<Crew {self.name} owner:{owner} size:{characters} seeking:{self.seeking}>'


class Request(db.Model):

    __tablename__ = 'requests'

    request_id = db.Column(db.Integer, primary_key=True)
    crew_id = db.Column(db.Integer, db.ForeignKey('crews.crew_id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    submit_time = db.Column(db.DateTime)

    def __init__(self, crew_id, character_id, message, submit_time=datetime.now):
        self.crew_id = crew_id
        self.character_id = character_id
        self.message = message
        self.submit_time = submit_time()

    
