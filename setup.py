def main():
    print("Setting up config file...")
    with open("config.ini", "w") as file:
        sg_api_key = input("Enter your SG API key: ")
        file.writelines("\n[SGCONFIG]\n")
        file.writelines("SGKEY = " + sg_api_key + "\n")


if __name__ == '__main__':
    main()