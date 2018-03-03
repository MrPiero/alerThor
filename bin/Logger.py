# https://github.com/sendgrid/sendgrid-python

import datetime
import sendgrid
import configparser
from sendgrid.helpers.mail import *


class Logger:
    def get_logger(self, type, sgkey=None):
        if type == "SG":
            if sgkey is None:
                cfg = configparser.ConfigParser()
                cfg.read("config.ini")
                return LoggerMail(cfg=cfg["SGCONFIG"])
            else:
                return LoggerMail(sgkey=sgkey)


class LoggerMail:
    def __init__(self, cfg=None, sgkey=None):
        if cfg is not None:
            self.sg = sendgrid.SendGridAPIClient(apikey=cfg["SGKEY"])
        elif sgkey is not None:
            self.sg = sendgrid.SendGridAPIClient(apikey=sgkey)
        else:
            self.sg = sendgrid.SendGridAPIClient(apikey=input("Enter SG API KEY"))
        self.config = cfg
        self.content = "<h2>Logged in RPi at {}</h2>".format(datetime.datetime.now().strftime("%c"))

    def send(self, sender="pi@yourhome.com",
             receiver="you@yourmail.com", subject="SSH Login Authorized", test=False):
        if not test:
            sender = self.config["DEFAULT_FROM"]
            receiver = self.config["DEFAULT_TO"]
        from_email = Email(sender)
        to_email = Email(receiver)
        content = Content("text/html", self.content)
        mail = Mail(from_email, subject, to_email, content)

        return self.sg.client.mail.send.post(request_body=mail.get())