from flask import Blueprint, flash, url_for, redirect, render_template
from flask_login.utils import login_required
from app.auth.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user
from app.models import User
from app import db
from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()
    
    if form.validate_on_submit():
        
        username = form.username.data
        password = form.password.data
        username_exists = User.query.filter_by(username=username).first()
        if username_exists:
            flash(f'The username "{username}" is already registered.', "warning")
            return render_template("register.html", form=form)
        user = User(username, password)
        db.session.add(user)
        db.session.commit()

        flash("You have registered successfully.")
        login_user(user)

        return redirect(url_for("users.user_profile", username = user.username))
    
    return render_template("register.html", form=form)




@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"Welcome back, {user.username}")
                return redirect(url_for('main.home'))
            else:
                flash("Incorrect password")
                return redirect(url_for('auth.login'))
        else: 
            flash('That username does not exist.')
            return redirect(url_for("main.login"))
    
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))

