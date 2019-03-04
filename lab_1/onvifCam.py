from onvif import ONVIFCamera
from time import sleep
import zeep


#some weird hack found on StackOverflow
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.AnySimpleType.pythonvalue = zeep_pythonvalue


class Camera:
    def __init__(self, ip, port, login, password):
        self.cam = ONVIFCamera(ip, port, login, password)
        print("Connected to camera ", ip, ":", port, sep="")
        self.ptz_service = self.cam.create_ptz_service()
        self.media_profile = self.cam.create_media_service().GetProfiles()[0] 
        # token here can be used for anything
        self.general_token = self.media_profile.token
    
    def getGeneralToken(self):
        return self.general_token

    def getStatus(self):
        Req = {'ProfileToken':  self.getGeneralToken()}
        return self.ptz_service.GetStatus(Req)
    
    def getPosition(self):
        position = self.getStatus().Position
        x = position.PanTilt.x
        y = position.PanTilt.y
        print('Cam position is: (', x,', ', y, ')', sep='')
        return position
    
    def absoluteMove(self, x, y):
        print("Perform absolute move to (", x,"," , y, ")", sep="")
        position = self.getPosition()
        position.PanTilt.x = x
        position.PanTilt.y = y
        Req = self.ptz_service.create_type("AbsoluteMove")
        Req.Position = position
        Req.ProfileToken = self.getGeneralToken()
        self.ptz_service.AbsoluteMove(Req)
        sleep(5) # kinda time-consuming operation
        
    def setFocus(self, value):
        print("Set focus to", value)
        imaging = self.cam.create_imaging_service()
        Req = imaging.create_type("Move")
        token = self.media_profile.VideoSourceConfiguration.SourceToken
        print(imaging.GetImagingSettings(token))
        print()
        Focus = imaging.GetMoveOptions(token)
        # Focus.Absolute = 0.5
        # Focus.Continuous = None
        print(Focus)
        Req.Focus = Focus
        Req.VideoSourceToken = token
        # Focus = {
        #     'Absolute': 0.5
        # }
        # Req.Focus = Focus
        print(Req)
        imaging.Move(Req)
