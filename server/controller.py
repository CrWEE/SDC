import RPi.GPIO as GPIO
from time import sleep

in1 = 20
in2 = 26
en = 16
temp1 = 1
left = 6
right = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(left, GPIO.OUT)
GPIO.setup(right, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
speed = 25
p.start(speed)

def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

def left():
    GPIO.output(right, GPIO.LOW)
    GPIO.output(left, GPIO.HIGH)

def right():
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.HIGH)

def straight():
    GPIO.output(left, GPIO.LOW)
    GPIO.output(right, GPIO.LOW)

def faster():
    global speed
    speed += 25
    p.ChangeDutyCycle(speed)

def slower():
    global speed
    speed -= 25
    p.ChangeDutyCycle(speed)
