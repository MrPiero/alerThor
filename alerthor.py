import configparser
import login_mail
import sys


def main():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    logger = login_mail.LoggerMail(sgkey=cfg["SGCONFIG"]["SGKEY"])
    logger.send(sender=sys.argv[1], receiver=sys.argv[2])


if __name__ == '__main__':
    main()
