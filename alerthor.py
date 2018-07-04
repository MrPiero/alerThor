from bin import Loggers


def main():
    logger = Loggers.logger_factory("SG")
    logger.log()


if __name__ == '__main__':
    main()
