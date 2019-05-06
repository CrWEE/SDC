import cv2
import numpy as np

def ORB_detector(image, original):
    imagebw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    orig_small = cv2.resize(original, None, fx=0.15, fy=0.15)
    orb = cv2.ORB_create(1000, 1.2)
    (kp1, desc1) = orb.detectAndCompute(imagebw, None)
    (kp2, desc2) = orb.detectAndCompute(orig_small, None)
    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(desc1, desc2)

    img3 = cv2.drawMatches(image, kp1, orig_small, kp2, matches, None, flags=2)
    print(len(matches))
    cv2.imshow('Final image', img3)
    return matches

image = cv2.imread('resources/stop1.jpg')
original = cv2.imread('resources/stop_original.jpg', 0)
cv2.imshow('Original Image', image)
cv2.waitKey(0)

matchesCalculated = ORB_detector(image, original)
cv2.waitKey(0)
cv2.destroyAllWindows()