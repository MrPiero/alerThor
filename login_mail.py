# https://github.com/sendgrid/sendgrid-python

import datetime
import sendgrid
import os
from sendgrid.helpers.mail import *


class LoggerMail:
    def __init__(self, sgkey=os.environ.get('SENDGRID_API_KEY')):
        self.sg = sendgrid.SendGridAPIClient(apikey=sgkey)
        self.content = "<h2>Logged in RPi at {}</h2>".format(datetime.datetime.now().strftime("%c"))

    def send(self, sender="pi@yourhome.com",
             receiver="you@yourmail.com", subject="SSH Login Authorized"):
        from_email = Email(sender)
        to_email = Email(receiver)
        content = Content("text/html", self.content)
        mail = Mail(from_email, subject, to_email, content)

        return self.sg.client.mail.send.post(request_body=mail.get())