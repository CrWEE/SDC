from picamera.array import PiRGBArray
from picamera import PiCamera
import struct # to send `int` as  `4 bytes`
import cv2


class CameraFeed:

    def __init__(self):
        self.sockets = []

    def add_socket(self, socket):
        self.sockets.append(socket)

    def remove_socket(self, socket):
        self.sockets.remove(socket)

    def send_images(self):
        print("Start sending images")
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        raw_capture = PiRGBArray(camera, size=(640, 480))

        # capture frames from the camera
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
            image = frame.array
            img_str = cv2.imencode('.jpg', image)[1].tostring()

            len_str = struct.pack('!i', len(img_str))
            for s in self.sockets:
                s.send(len_str)
                s.send(img_str)

            raw_capture.truncate(0)
