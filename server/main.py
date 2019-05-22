import bus
import receiver
import atexit
import RPi.GPIO as GPIO
import camera.video_connections as videocon
import threading

def exit_handler():
    GPIO.cleanup()

def main():
    bus.init_buses()
    atexit.register(exit_handler)
    threading.Thread(target=videocon.start_video_connection).start()
    threading.Thread(target=receiver.start_receiving).start()

main()
