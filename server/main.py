import bus
import receiver
import atexit
import RPi.GPIO as GPIO

def exit_handler():
    GPIO.cleanup()

def main():
    bus.init_buses()
    atexit.register(exit_handler)
    receiver.start_receiving()

main()
