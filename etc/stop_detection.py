import cv2
import numpy as np


def detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

    for (x, y, w, h) in bodies:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

    image = cv2.flip(image,1)
    return image


body_classifier = cv2.CascadeClassifier('resources/Stopsign_HAAR_19Stages.xml')
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    cv2.imshow('Our Face Extractor', detect(frame))
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()