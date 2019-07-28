import bus
import atexit
import RPi.GPIO as GPIO
import camera.connections as videocon
import threading
import detection.cascade_classifier.stop_detection as stop_detection
from bus_listener import BusListener
from camera.camera import CameraFeed

# To avoid GCed because of the weak reference in the bus
bus_listener = BusListener()


def exit_handler():
    GPIO.cleanup()


def main():
    bus.init_buses(bus_listener)

    camera_feed = CameraFeed()
    threading.Thread(target=videocon.start_video_connection, args=[camera_feed]).start()
    threading.Thread(target=stop_detection.start_detection_from_camera_feed, args=[camera_feed]).start()
    atexit.register(exit_handler)


main()
