from bin import Logger


def main():
    factory = Logger.Logger()
    logger = factory.get_logger("SG")
    logger.send()


if __name__ == '__main__':
    main()
