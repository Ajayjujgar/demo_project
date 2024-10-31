import logging


class LogGenerator:
    @staticmethod
    def loggen():
        logfile = logging.FileHandler("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\Logs"
                                      "\\Automation testing.log")
        Format = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s -	%(lineno)s - %(message)s")
        logfile.setFormatter(Format)
        logger = logging.getLogger()
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
