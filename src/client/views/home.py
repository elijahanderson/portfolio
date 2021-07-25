from flask import Blueprint, render_template, session

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/')
def home():
    """ REST endpoint for the home page. """
    return render_template('home.html')
