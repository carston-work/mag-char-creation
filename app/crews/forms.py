from flask_wtf.form import FlaskForm
from flask_login import current_user
from app.characters.forms import MultiCheckBoxField
from wtforms.fields import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length


class CrewForm(FlaskForm):
    name = StringField("Crew Name: ", 
                        validators=[
                            InputRequired("Your crew must have a name"),
                            DataRequired("Your crew's name cannot be blank")
                        ])
    preferences = MultiCheckBoxField("Preferences: ", choices=[("action",'Action'), ("adventure",'Adventure'), ("side-quests",'Side Quests'), ("character-driven","Character Driven"), ("plot-driven",'Plot Driven')])
    seeking = BooleanField("Looking for new crew members?")
    submit = SubmitField("Create Crew")


class RequestForm(FlaskForm):
    
    character_id = SelectField("Character", choices=[(None, "Select a character")], validators=[
        InputRequired("You must select a character")
    ])
    message = StringField("Message: ", validators=[
    InputRequired("You must submit a message."),
    DataRequired("You must submit a message"),
    Length(message="Your message must be between 10 and 255 characters long", min=10, max=255)
    ])
    submit = SubmitField("Submit Request")