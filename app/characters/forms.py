from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms.fields import StringField, SubmitField, SelectMultipleField, IntegerField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length
from wtforms.widgets.core import Input


class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget=widgets.CheckboxInput()


class CharacterForm(FlaskForm):
    name = StringField("Character Name: ", 
                        validators=[
                            InputRequired("Your character must have a name"),
                            DataRequired("Your character's name cannot be blank"),
                            Length(min=1, max=30, message="This field must contain between 1 and 30 characters")
                        ])
    concept = StringField("Character Concept", 
                        validators=[
                            InputRequired("Your character must have a concept"),
                            DataRequired("Your character's concept cannot be blank"),
                            Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
                        ])
    preferences = MultiCheckBoxField("Preferences: ", choices=[("action",'Action'), ("adventure",'Adventure'), ("side-quests",'Side Quests'), ("character-driven","Character Driven"), ("plot-driven",'Plot Driven')])
    race = SelectField("Race: ", choices=[('noble', "Noble"),('skaa', "Skaa"),('terris', "Terris")], validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
    ])
    sex = StringField("Gender: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=10, message="This field must contain between 1 and 10 characters")
    ])
    age = IntegerField("Age: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=25,)
    height = IntegerField("Height: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=65)
    weight = IntegerField("Weight: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=100)
    physique = IntegerField("Physique", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    charm = IntegerField("Charm: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    wits = IntegerField("Wits: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    resources = IntegerField("Resources: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    influence = IntegerField("Influence: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    spirit = IntegerField("Spirit: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=2)
    health = IntegerField("Health: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=4)
    reputation = IntegerField("Reputation: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=4)
    willpower = IntegerField("Willpower: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired("This field must be filled")],
        default=4)
    drive = StringField("Drive: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
    ])
    profession = StringField("Profession: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
    ])
    specialty = StringField("Specialty: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
    ])
    feature = StringField("Distinguishing Feature: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
    ])
    personality = StringField("Personality: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=40, message="This field must contain between 1 and 40 characters")
    ])
    tragedy = StringField("Tragedy: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=128, message="This field must contain between 1 and 128 characters")
    ])
    destiny = StringField("Destiny: ", validators=[
        InputRequired("This field must be filled"),
        DataRequired('This field must be filled'),
        Length(min=1, max=128, message="This field must contain between 1 and 128 characters")
    ])
    powers = SelectField("Powers", choices=[("none", "None"), ("mimicry", "Mimicry"), ("misting", "Misting"), ("mistborn", "Mistborn"), ("keeper", "Keeper")], validators=[
        InputRequired("This field must be filled")
    ])
    submit = SubmitField("Create Character")