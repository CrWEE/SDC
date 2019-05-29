import bus
import atexit
import RPi.GPIO as GPIO
import camera.connections as videocon
import threading
from bus_listener import BusListener
from camera.camera import CameraFeed


def exit_handler():
    GPIO.cleanup()


def main():
    camera_feed = CameraFeed()
    bus_listener = BusListener(camera_feed)
    bus.init_buses(bus_listener)

    atexit.register(exit_handler)

    threading.Thread(target=videocon.start_video_connection).start()
    threading.Thread(target=camera_feed.send_images()).start()


main()
