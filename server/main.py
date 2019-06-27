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
    bus_listener = BusListener()
    bus.init_buses(bus_listener)

    camera_feed = CameraFeed()
    threading.Thread(target=videocon.start_video_connection, args=[camera_feed]).start()

    atexit.register(exit_handler)


main()
