import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def ApplicationUrl():
        url =(config.get('commoninfo','baseUrl'))
        return url
    @staticmethod
    def getLoginEmail():
        email = config.get('commoninfo','email')
        return email
    @staticmethod
    def getUserPwd():
        password = config.get('commoninfo','password')
        return password

