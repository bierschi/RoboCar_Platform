import picamera


class Camera:

    def __init__(self):

        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.camera.rotation = 180
        pass
