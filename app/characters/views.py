from flask import render_template, redirect, Blueprint, url_for
from flask_login import login_required, current_user
from app.models import Character
from app.characters.forms import CharacterForm
from app import db

char = Blueprint('char', __name__, template_folder="templates")

@char.route("/create", methods=["GET", "POST"])
@login_required
def create_new():
    form = CharacterForm()

    if form.validate_on_submit():

        name = form.name.data
        concept = form.concept.data
        creator_id = current_user.user_id
        

        preferences = form.preferences.data
        preferences_int = 0
        if 'action' in preferences:
            preferences_int += 16
        if "adventure" in preferences:
            preferences_int += 8
        if 'side-quests' in preferences:
            preferences_int += 4
        if 'character-driven' in preferences:
            preferences_int += 2
        if 'plot-driven' in preferences:
            preferences_int += 1

        new_char = Character(creator_id, name, concept, preferences_int)
        db.session.add(new_char)
        db.session.commit()

        return redirect(url_for("users.user_profile", username=current_user.username))

    return render_template("new_character.html", form=form)
