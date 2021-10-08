from flask import Blueprint, flash, url_for, redirect
from app.auth.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user
from app.models import User
from app import db

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User(username, password)
        db.session.add(user)
        db.session.commit()

        flash("You have registered successfully.")
        login_user(user)

        return redirect(url_for("main.home"))




@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

