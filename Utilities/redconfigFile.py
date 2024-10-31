import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\Configuration\\config.ini")


class ReadConfigfile:
    @staticmethod
    def getUsername():
        Username = config.get("common data", "Username")
        return Username

    @staticmethod
    def getPassword():
        Password = config.get("common data", "Password")
        return Password

    @staticmethod
    def username():
        userName = config.get("All data", "Username")
        return userName

    @staticmethod
    def password():
        password = config.get("All data", "Password")
        return password
