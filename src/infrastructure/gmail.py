import smtplib
import yaml

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_message(sender, to, subject, content):
    """ Create a message for an email. """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    message.attach(MIMEText(content, 'plain'))
    return message


def send_gmail(email_to, subject, content):
    with open('config/application.yml', 'r') as yml:
        config = yaml.safe_load(yml)
        gmail_pass = config['gmail_pass']
        address = config['gmail_address']
    message = create_message(address, address, subject, content)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(address, gmail_pass)
    session.sendmail(address, address, message.as_string())
    session.quit()

