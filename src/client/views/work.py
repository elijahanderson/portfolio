from flask import Blueprint, render_template, session
  
work_bp = Blueprint('work', __name__, template_folder='templates')


@work_bp.route('/work')
def work():
    """ REST endpoint for the home page. """
    return render_template('work.html', title='Work')
