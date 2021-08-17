from flask import Flask, session

from client.views.home import home_bp
from client.views.work import work_bp
from client.views.blog import blog_bp
from client.views.contact import contact_bp

""" Initialize the app. """
app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(work_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(contact_bp)
app.secret_key = "secret key"
