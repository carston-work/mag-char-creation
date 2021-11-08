from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_required, current_user
from app.models import Crew
from app.crews.forms import CrewForm
from app import db

crew = Blueprint('crew', __name__, template_folder="templates")

@crew.route('/create', methods=["GET", "POST"])
@login_required
def add_crew():
    form = CrewForm()

    if form.validate_on_submit():

        name = form.name.data
        seeking = form.seeking.data
        owner_id = current_user.user_id

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

        new_crew = Crew(owner_id, name, seeking, preferences_int)

        db.session.add(new_crew)
        db.session.commit()

        return redirect(url_for("users.user_profile", username=current_user.username))
    
    return render_template("add_crew.html", form=form)


@crew.route('/search/<char_prefs>')
def search(char_prefs=0):
    char_prefs = int(char_prefs)
    def pref_order(item):
        key = bin(int(char_prefs))[2:]
        search = bin(item.preferences)[2:]
        count_same = 0
        langth = min(len(key), len(search))
        for i in range(-1, -1-langth, -1):
            if key[i] == search[i]:
                count_same += 1
        return bin(item.preferences ^ char_prefs).count('1') - count_same
    crews = Crew.query.filter(Crew.seeking==True, Crew.owner_id != current_user.user_id).order_by(Crew.preferences)
    crews = sorted(crews, key=pref_order)
    return render_template('search_crews.html', crews=crews, pref=char_prefs)