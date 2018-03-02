def main():
    print("Setting up config file...")
    with open("config.yml", "w") as file:
        sg_api_key = input("Enter your SG API key: ")
        file.writelines("sgconfig:")
        file.writelines("\n\tsgkey: " + sg_api_key)


if __name__ == '__main__':
    main()