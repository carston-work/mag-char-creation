from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user
from app.models import User


from app import db

users = Blueprint('users', __name__, template_folder="templates")


@users.route("/profile/<username>")
def user_profile(username):
    if current_user == User.query.filter_by(username=username).first():
        return render_template("profile.html")
    else:
        flash("You do not have permission to view that page")
        return redirect(url_for("main.home"))
