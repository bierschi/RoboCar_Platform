import picamera
import socket
from time import sleep


class Camera:

    def __init__(self):

        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.camera.rotation = 180

    def start_recording(self, conn):
        """

        :return:
        """
        self.camera.start_recording(output=conn, format='h264')

    def server(self):

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8001))
        server_socket.listen(0)

        # Accept a single connection and make a file-like object out of it
        connection = server_socket.accept()[0].makefile('wb')
        try:
            self.camera.start_recording(connection, format='h264')
            while True:
                sleep(1)
            #self.camera.wait_recording(60)
            #self.camera.stop_recording()
        finally:
            connection.close()
            server_socket.close()


if __name__ == '__main__':
    ccamera = Camera()
    ccamera.server()
