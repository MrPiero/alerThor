from os.path import expanduser
home = expanduser("~")
alerThor_home = home + "/alerThor/"

def main():
    print("Setting up config file...")
    with open(alerThor_home + "config.ini", "w") as file:
        sg_api_key = input("Enter your SG API key: ")
        sender = input("Enter your default sender email (custom): ")
        receiver = input("Enter default receiver email: ")
        file.writelines("\n[SGCONFIG]\n")
        file.writelines("SGKEY = " + sg_api_key + "\n")
        file.writelines("DEFAULT_FROM = " + sender + "\n")
        file.writelines("DEFAULT_TO = " + receiver + "\n")


if __name__ == '__main__':
    main()
