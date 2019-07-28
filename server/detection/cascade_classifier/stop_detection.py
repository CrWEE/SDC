import cv2
import time
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../../resources/Stopsign_HAAR_19Stages.xml')
stop_classifier = cv2.CascadeClassifier(filename)


def detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = stop_classifier.detectMultiScale(gray, 1.2, 3)
    return detections


def draw(frame, detections):
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    return frame


def start_detection_from_camera_feed(camera_feed):
    time.sleep(3)  # Wait for camera init
    print("STOP sign cascade classifier started")
    while True:
        # cv2.imshow('Our Face Extractor', detect(frame))
        detections = detect(camera_feed.frame.array[:])
        if len(detections) > 0:
            print("Found %d STOP sign!" % len(detections))
        time.sleep(1/camera_feed.frame_rate)
