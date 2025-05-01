# read common data from ini file
# so we have special pkg configparser in python - inside it method called RawConfigParser
# it is having some methods we can call other method

import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password