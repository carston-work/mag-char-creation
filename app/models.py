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
    race = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    physique = db.Column(db.Integer, nullable=False)
    charm = db.Column(db.Integer, nullable=False)
    wits = db.Column(db.Integer, nullable=False)
    resources = db.Column(db.Integer, nullable=False)
    resources_temp = db.Column(db.Integer, nullable=False)
    influence = db.Column(db.Integer, nullable=False)
    influence_temp = db.Column(db.Integer, nullable=False)
    spirit = db.Column(db.Integer, nullable=False)
    spirit_temp = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    health_temp = db.Column(db.Integer, nullable=False)
    reputation = db.Column(db.Integer, nullable=False)
    reputation_temp = db.Column(db.Integer, nullable=False)
    willpower = db.Column(db.Integer, nullable=False)
    willpower_temp = db.Column(db.Integer, nullable=False)
    drive = db.Column(db.String(40), nullable=False)
    profession = db.Column(db.String(40), nullable=False)
    specialty = db.Column(db.String(40), nullable=False)
    feature = db.Column(db.String(40), nullable=False)
    personality = db.Column(db.String(40), nullable=False)
    tragedy = db.Column(db.String(128), nullable=False)
    destiny = db.Column(db.String(128), nullable=False)
    powers = db.Column(db.PickleType, nullable=False)
    equipment = db.Column(db.PickleType, nullable=False)

    def __init__(self, 
        creator_id, 
        name, 
        concept, 
        preferences, 
        race, 
        sex, 
        age, 
        height, 
        weight, 
        physique, 
        charm, 
        wits,
        resources,
        resources_temp,
        influence,
        influence_temp,
        spirit,
        spirit_temp,
        health,
        health_temp,
        reputation,
        reputation_temp,
        willpower,
        willpower_temp,
        drive,
        profession,
        specialty,
        feature,
        personality,
        tragedy,
        destiny,
        powers
        ):
        self.creator_id = creator_id
        self.name = name
        self.concept = concept
        self.preferences = preferences
        self.race = race
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.physique = physique
        self.charm = charm
        self.wits = wits
        self.resources = resources
        self.resources_temp = resources_temp
        self.influence = influence
        self.influence_temp = influence_temp
        self.spirit = spirit
        self.spirit_temp = spirit_temp
        self.health = health
        self.health_temp = health_temp
        self.reputation = reputation
        self.reputation_temp = reputation_temp
        self.willpower = willpower
        self.willpower_temp = willpower_temp
        self.drive = drive
        self.profession = profession
        self.specialty = specialty
        self.feature = feature
        self.personality = personality
        self.tragedy = tragedy
        self.destiny = destiny
        self.powers = powers

    def __repr__(self):
        creator = self.creator.username
        return f'Character: {self.name}, {self.concept} creator: {creator}'

    request = db.relationship("Request", uselist=False, backref="character", lazy=True)


class Crew(db.Model):

    __tablename__ = "crews"

    crew_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(40), nullable=False, unique=True)
    seeking = db.Column(db.Boolean, nullable=False)
    preferences = db.Column(db.Integer, nullable = False)
    cause = db.Column(db.String(15), nullable=False)
    target = db.Column(db.String(15), nullable=False)
    method = db.Column(db.String(15), nullable=False)

    def __init__(self, owner_id, name, seeking, preferences, cause, target, method):
        self.owner_id = owner_id
        self.name = name
        self.seeking = seeking
        self.preferences = preferences
        self.cause = cause
        self.target = target
        self.method = method

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

    
