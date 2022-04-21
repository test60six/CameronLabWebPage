# pip install flask-bootstrap

import flask
from flask import Flask
from flask_bootstrap import Bootstrap



# import smtplib
# from email.message import EmailMessage
# from string import template
# from pathlib import Path

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

html= Template(Path("contact.html").read_text())

email= EmailMessage()
email["from"] = "input"
email["to"] = "Lab email here"
email["subject"]= "input"


email.set_content(html.substitute({name:"Cameron",}),"html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email address here","password here")
    smtp.send_message(email)
    print(" Thank you! Your message hasd been sent!")
