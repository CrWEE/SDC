from picamera.array import PiRGBArray
from picamera import PiCamera
import threading
import io
import cv2


class CameraFeed:

    frame_rate = 24

    def __init__(self):
        self.thread = threading.Thread(target=self._record_image)
        self.thread.daemon = True
        self.thread.start()
        self.image = None
        self.frame = None

    def _record_image(self):
        print("Start sending images")
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = self.frame_rate
        array = PiRGBArray(camera, size=(640, 480))

        # capture frames from the camera
        for frame in camera.capture_continuous(array, format="bgr", use_video_port=True):
            self.frame = frame  # To use the frame locally
            self._process_frame(frame)
            array.truncate(0)


    def _process_frame(self, frame):
        ret, jpeg = cv2.imencode('.jpeg', frame.array)
        self.image = jpeg

