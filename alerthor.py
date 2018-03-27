from bin import Loggers


def main():
    factory = Loggers.LoggerFactory()
    logger = factory.get_logger("SG")
    logger.log()


if __name__ == '__main__':
    main()
