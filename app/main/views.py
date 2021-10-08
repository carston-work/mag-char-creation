from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user

main = Blueprint('main', __name__, template_folder="templates")

# def root():
#     return redirect(url_for("main.home"))

@main.route('/')
def home():
    return render_template('home.html')