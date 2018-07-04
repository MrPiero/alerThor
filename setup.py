def main():
    print("Setting up config file...")
    with open("config.ini", "w") as file:
        sg_api_key = input("Enter your SG API key: ")
        sender = input("Enter your sender email (custom): ")
        receiver = input("Enter receiver email: ")
        file.writelines("\n[SGCONFIG]\n")
        file.writelines("SGKEY = " + sg_api_key + "\n")
        file.writelines("DEFAULT_FROM = " + sender + "\n")
        file.writelines("DEFAULT_TO = " + receiver + "\n")


if __name__ == '__main__':
    main()
