from flask import Blueprint, render_template, url_for, redirect, current_app, request as req
from flask.helpers import flash
from flask_login import login_required, current_user
from app.models import Crew, Request
from app.crews.forms import CrewForm, RequestForm
from app import db
import json

crew = Blueprint('crew', __name__, template_folder="templates")
app = current_app

@crew.route('/create', methods=["GET", "POST"])
@login_required
def add_crew():
    form = CrewForm()

    if form.validate_on_submit():

        name = form.name.data
        crew_exists = Crew.query.filter_by(name=name).first()
        if crew_exists:
            flash("That Crew name is taken. Please use a different one.")
        else:
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


@crew.route('/send_request/<crew_id>', methods=['GET', 'POST'])
@login_required
def send_request(crew_id):
    form = RequestForm()
    chars = [(str(char.character_id), char.name) for char in current_user.characters if not char.crew]
    form.character_id.choices = chars

    if form.validate_on_submit():
        new_request = Request(crew_id, form.character_id.data, form.message.data)
        db.session.add(new_request)
        db.session.commit()
        flash("Request successfully sent")
        return redirect(url_for('users.user_profile', username=current_user.username))
    
    return render_template('send_request.html', form=form)


@crew.route('/view_crew/<crew_id>')
def view_crew(crew_id):
    crew = Crew.query.get(crew_id)
    if crew:
        return render_template('view_crew.html', crew=crew)
    else:
        flash("That crew doesn't exist")
        return redirect(url_for('main.home'))


@crew.route('/requests/<request_id>', methods=['GET', 'PUT', 'DELETE'])
def get_request_message(request_id):
    my_request = Request.query.get(request_id)
    if my_request:
        if req.method == "PUT":
            my_request.character.crew_id = my_request.crew.crew_id
            db.session.delete(my_request)
        elif req.method == "DELETE":
            db.session.delete(my_request)
        else:
            return json.dumps(my_request.message)

        db.session.commit()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    return json.dumps({'success':False}), 400, {'ContentType':'application/json'}