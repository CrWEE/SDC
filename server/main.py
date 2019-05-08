import bus
import receiver
import atexit
import RPi.GPIO as GPIO
import camera.send_video as video
import threading

def exit_handler():
    GPIO.cleanup()

def main():
    bus.init_buses()
    atexit.register(exit_handler)
    threading.Thread(target=video.start_connections).start()
    receiver.start_receiving()

main()
