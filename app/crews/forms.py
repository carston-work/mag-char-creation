from flask_wtf.form import FlaskForm
from app.characters.forms import MultiCheckBoxField
from wtforms.fields import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, DataRequired, ValidationError


class CrewForm(FlaskForm):
    name = StringField("Crew Name: ", 
                        validators=[
                            InputRequired("Your crew must have a name"),
                            DataRequired("Your crew's name cannot be blank")
                        ])
    preferences = MultiCheckBoxField("Preferences: ", choices=[("action",'Action'), ("adventure",'Adventure'), ("side-quests",'Side Quests'), ("character-driven","Character Driven"), ("plot-driven",'Plot Driven')])
    seeking = BooleanField("Looking for new crew members?")
    submit = SubmitField("Create Crew")