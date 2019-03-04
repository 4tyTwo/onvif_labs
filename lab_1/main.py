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

def getQuater(x, y):
    if (x > 0):
        if (y > 0):
            return 1
        return 2
    else:
        if (y > 0):
            return 4
        return 3

def getOppositeCorner(x, y):
    quater = getQuater(x, y)
    if (quater == 1):
        return (-1, -1)
    if (quater == 2):
        return (-1, 1)
    if (quater == 4):
        return (1, -1)
    return (1, 1)


def runTest(ip, port, login, password):
    cam = Camera(ip, port, user.login, user.password)
    pos = cam.getPosition()
    origin_x = pos.PanTilt.x
    origin_y = pos.PanTilt.y
    dest_pos = getOppositeCorner(origin_x, origin_y)
    cam.absoluteMove(dest_pos[0], dest_pos[1])
    cam.getPosition()
    sleep(5)
    cam.absoluteMove(origin_x, origin_y) # return cam to it's origin

user = getCredentials('credentials')
ip = '192.168.15.42'
port = 80
streamPort = 554
thread = Thread(target=runTest, args=(ip, port, user.login, user.password, ))
thread.start()
captureStream('rtsp', user.login, user.password, ip,
              streamPort, '/Streaming/channels/101')
