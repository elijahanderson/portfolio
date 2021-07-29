from flask import Blueprint, render_template, request, session
from traceback import print_exc

from infrastructure.gmail import send_gmail

contact_bp = Blueprint('contact', __name__, template_folder='templates')


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """ REST endpoint for the contact page. """
    if request.method == 'POST':
        name = request.form['contact-name']
        email = request.form['contact-email']
        body = request.form['contact-body']
        try:
            email_body = f"Name: {name}\nEmail: {email}\n{body}\n"
            send_gmail('dispentia@gmail.com', 'Portfolio Contact Notification', email_body)
            return render_template('contact.html', title='Contact', success=True)
        except Exception as e:
            print_exc()
            error_msg = "An error occurred while trying to send your information. Please wait a minute or two, " \
                        "refresh the page, and try again."
            send_gmail('dispentia@gmail.com', 'Portfolio Error Notification', 
                    f"Porfolio contact page error: {str(e)}")
            return render_template('contact.html', title='Contact', error_msg=error_msg)
    return render_template('contact.html', title='Contact')

