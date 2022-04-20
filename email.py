import flask

import smtplib
from email.message import EmailMessage
from string import template
from pathlib import Path

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
