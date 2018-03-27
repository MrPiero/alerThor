# https://github.com/sendgrid/sendgrid-python

import datetime
import sendgrid
import configparser
import os.path
from sendgrid.helpers.mail import *


class LoggerFactory:
    def get_logger(self, logger_type, sgkey=None):
        if logger_type == "SG":
            if os.path.isfile("config.ini"):
                cfg = configparser.ConfigParser()
                cfg.read("config.ini")
                return LoggerMail(cfg=cfg["SGCONFIG"])
            elif sgkey is not None:
                return LoggerMail(sgkey=sgkey)
            else:
                return LoggerMail()


class Logger:
    def log(self):
        pass


class LoggerMail(Logger):
    def __init__(self, cfg=None, sgkey=None):
        if cfg is not None:
            self.sg = sendgrid.SendGridAPIClient(apikey=cfg["SGKEY"])
        elif sgkey is not None:
            self.sg = sendgrid.SendGridAPIClient(apikey=sgkey)
        else:
            self.sg = sendgrid.SendGridAPIClient(apikey=input("Enter SG API KEY"))
        self.config = cfg
        self.content = "<h2>Logged in RPi at {}</h2>".format(datetime.datetime.now().strftime("%c"))

    def log(self, sender="pi@yourhome.com",
            receiver="you@yourmail.com", subject="SSH Login Authorized", test=False):
        if not test:
            sender = self.config["DEFAULT_FROM"]
            receiver = self.config["DEFAULT_TO"]
        from_email = Email(sender)
        to_email = Email(receiver)
        content = Content("text/html", self.content)
        mail = Mail(from_email, subject, to_email, content)

        return self.sg.client.mail.send.post(request_body=mail.get())