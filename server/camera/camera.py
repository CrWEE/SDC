from picamera.array import PiRGBArray
from picamera import PiCamera
import struct # to send `int` as  `4 bytes`
import time
import cv2


class CameraFeed:

    def __init__(self, socket):
        self.socket = socket

    def send_images(self):
        print("Start sending images")
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        raw_capture = PiRGBArray(camera, size=(640, 480))

        # capture frames from the camera
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            img_str = cv2.imencode('.jpg', image)[1].tostring()

            print('len:', len(img_str))

            len_str = struct.pack('!i', len(img_str))
            self.socket.send(len_str)
            self.socket.send(img_str)
            # clear the stream in preparation for the next frame
            #time.sleep(0.5)
            raw_capture.truncate(0)
