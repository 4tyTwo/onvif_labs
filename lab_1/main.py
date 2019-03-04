from onvif import ONVIFCamera
import zeep
from time import sleep
from onvifCam import Camera
from threading import Thread
from streaming import captureStream

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

def runTest(ip, port, login, password):
    cam = Camera(ip, port, user.login, user.password)
    pos = cam.getPosition()
    x = pos.PanTilt.x
    y = pos.PanTilt.y
    cam.absoluteMove(-1, -1)
    cam.getPosition()
    cam.absoluteMove(x, y) # return cam to is's origin

user = getCredentials('credentials')
ip = '192.168.15.42'
port = 80
streamPort = 554
thread = Thread(target=runTest, args=(ip, port, user.login, user.password, ))
thread.start()
captureStream('rtsp', user.login, user.password, ip,
              streamPort, '/Streaming/channels/101')
