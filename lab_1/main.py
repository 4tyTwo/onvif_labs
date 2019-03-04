from onvif import ONVIFCamera
import zeep
from time import sleep
from onvifCam import Camera

def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.AnySimpleType.pythonvalue = zeep_pythonvalue

class Credentials:

    login = ""
    password = ""

    def __init__(self, login, password):
        self.login = login
        self.password = password
        

def getCredentials(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
    f.close()
    content = list(map(lambda st: st[ : -1], content))
    return Credentials(content[0], content[1])

user = getCredentials('credentials')
ip = '192.168.15.42'
port = 80
cam = Camera(ip, port, user.login, user.password)
cam.getPosition()
cam.absoluteMove(-1, -1)
cam.getPosition()
cam.setFocus(1)
