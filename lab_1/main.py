from onvif import ONVIFCamera
import zeep
from time import sleep
from onvifCam import Camera
# from camera import Camera

def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.AnySimpleType.pythonvalue = zeep_pythonvalue

class Credentials:

    login = ""
    password = ""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        

def getCredentials():
    username = input("Username:")
    password = input("Password:")
    return Credentials(username, password)


ip = '192.168.15.42'
port = 80
login = "iigortoporkov"
password = "FP72Ainc6pwRLsrT"
cam = Camera(ip, port, login, password)
# cam.getPosition()
# cam.absoluteMove(-1, -1)
# cam.getPosition()
cam.setFocus(1)
