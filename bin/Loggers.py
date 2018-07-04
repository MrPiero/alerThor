# https://github.com/sendgrid/sendgrid-python

import datetime
import sendgrid
import configparser
import os.path
import platform
from sendgrid.helpers.mail import *


def get_sg(cfg, sgkey):
    if cfg is not None:
        return sendgrid.SendGridAPIClient(apikey=cfg["SGKEY"])
    elif sgkey is not None:
        return sendgrid.SendGridAPIClient(apikey=sgkey)
    else:
        return sendgrid.SendGridAPIClient(apikey=input("Enter SG API KEY"))


def logger_factory(logger_type, sgkey=None):
    if logger_type == "SG":
        if os.path.isfile("config.ini"):
            cfg = configparser.ConfigParser()
            cfg.read("config.ini")
            return LoggerMail(cfg=cfg["SGCONFIG"])
        elif sgkey is not None:
            return LoggerMail(sgkey=sgkey)
        else:
            return LoggerMail()


def get_content():
    system = platform.system()
    node = platform.node()
    time = datetime.datetime.now().strftime("%c")
    content = "A new SSH login was authorized to the following server:\n" \
                "\n\tSystem: {}" \
                "\n\tNode: {}" \
                "\n\tDatetime: {}".format(system, node, time)
    return content


class Logger:
    def log(self):
        pass


class LoggerMail(Logger):
    def __init__(self, cfg=None, sgkey=None):
        self.sg = get_sg(cfg, sgkey)
        self.config = cfg
        self.content = get_content()

    def log(self, sender="pi@yourhome.com", receiver="you@yourmail.com", subject="SSH Login Authorized", test=False):
        if not test:
            sender = self.config["DEFAULT_FROM"]
            receiver = self.config["DEFAULT_TO"]
        from_email = Email(sender)
        to_email = Email(receiver)
        content = Content("text/html", self.content)
        mail = Mail(from_email, subject, to_email, content)

        return self.sg.client.mail.send.post(request_body=mail.get())