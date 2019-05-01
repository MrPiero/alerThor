# https://github.com/sendgrid/sendgrid-python

import datetime
import sendgrid
import configparser
import os.path
import platform
import getpass
from sendgrid.helpers.mail import *

home = os.path.expanduser("~")
alerThor_home = home + "/alerThor/"
path_alerThor_config = alerThor_home + "config.ini"


def get_sg(cfg, sgkey):
    if cfg is not None:
        return sendgrid.SendGridAPIClient(api_key=cfg["SGKEY"])
    elif sgkey is not None:
        return sendgrid.SendGridAPIClient(api_key=sgkey)
    else:
        return sendgrid.SendGridAPIClient(api_key=input("Enter SG API KEY"))


def logger_factory(logger_type, sgkey=None):
    if logger_type == "SG":
        if os.path.isfile(path_alerThor_config):
            cfg = configparser.ConfigParser()
            cfg.read(path_alerThor_config)
            return LoggerMail(cfg=cfg["SGCONFIG"])
        elif sgkey is not None:
            return LoggerMail(sgkey=sgkey)
        else:
            return LoggerMail()


def get_content():
    system = platform.system()
    node = platform.node()
    time = datetime.datetime.now().strftime("%c")
    content = """
            A new SSH login was authorized to the following server:\n
                \n\tSystem: %s
                \n\tNode: %s
                \n\tUser: %s
                \n\tDatetime: %s
            """ % (system, node, getpass.getuser(), time)
    return content


class Logger:
    def log(self):
        pass


class LoggerMail(Logger):
    def __init__(self, cfg=None, sgkey=None):
        self.sg = get_sg(cfg, sgkey)
        self.config = cfg
        self.content = get_content()

    def log(self, sender=None, receiver=None, subject=None, content=None):
        from_email = self.config["DEFAULT_FROM"] if sender is None else sender
        to_email = self.config["DEFAULT_TO"] if receiver is None else receiver
        subject = "New SSH Login" if subject is None else subject
        content = self.content if content is None else content
        
        mail = Mail(from_email= from_email, to_emails=to_email, subject=subject, plain_text_content=content)

        return self.sg.client.mail.send.post(request_body=mail.get())
        