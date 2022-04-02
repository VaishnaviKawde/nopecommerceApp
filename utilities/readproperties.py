import configparser

config = configparser.RawConfigParser()

config.read(".\\configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('COMMON INFO','baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('COMMON INFO','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('COMMON INFO','password')
        return password