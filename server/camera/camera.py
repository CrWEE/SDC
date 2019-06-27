from picamera.array import PiRGBArray
from picamera import PiCamera
import threading
import io

class CameraFeed:

    def __init__(self):
        self.thread = threading.Thread(target=self._record_image)
        self.thread.daemon = True
        self.thread.start()
        self.image = None

    def _record_image(self):
        print("Start sending images")
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        # capture frames from the camera
        for frame in camera.capture_continuous(stream, format="jpeg", use_video_port=True):
            stream.seek(0)
            self.image = stream.read()
            stream.seek(0)
            stream.truncate(0)


