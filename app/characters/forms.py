from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms.fields import StringField, BooleanField, SubmitField, SelectMultipleField
from wtforms.validators import InputRequired, DataRequired, ValidationError


class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget=widgets.CheckboxInput()


class CharacterForm(FlaskForm):
    name = StringField("Character Name: ", 
                        validators=[
                            InputRequired("Your character must have a name"),
                            DataRequired("Your character's name cannot be blank")
                        ])
    concept = StringField("Character Concept", 
                        validators=[
                            InputRequired("Your character must have a concept"),
                            DataRequired("Your character's concept cannot be blank")
                        ])
    preferences = MultiCheckBoxField("Preferences: ", choices=[("action",'Action'), ("adventure",'Adventure'), ("side-quests",'Side Quests'), ("character-driven","Character Driven"), ("plot-driven",'Plot Driven')])
    submit = SubmitField("Create Character")