import RPi.GPIO as GPIO

in1 = 12
in2 = 6
en = 16
temp1 = 1
l1 = 26
r1 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(l1, GPIO.OUT)
GPIO.setup(r1, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(l1, GPIO.LOW)
GPIO.output(r1, GPIO.LOW)
p = GPIO.PWM(en, 1000)
speed = 100
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
    GPIO.output(r1, GPIO.LOW)
    GPIO.output(l1, GPIO.HIGH)

def right():
    GPIO.output(l1, GPIO.LOW)
    GPIO.output(r1, GPIO.HIGH)

def straight():
    GPIO.output(l1, GPIO.LOW)
    GPIO.output(r1, GPIO.LOW)

def faster():
    global speed
    speed += 25
    p.ChangeDutyCycle(speed)

def slower():
    global speed
    speed -= 25
    p.ChangeDutyCycle(speed)
