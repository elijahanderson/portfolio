from flask import Blueprint, render_template, session
  
about_bp = Blueprint('about', __name__, template_folder='templates')


@about_bp.route('/about')
def about():
    """ REST endpoint for the home page. """
    return render_template('about.html', title='About')
