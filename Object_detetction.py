# Python code for Multiple Color Detection
import img as img
import numpy as np
import cv2

# Capturing video through webcam
framewidth = 640
frameheight = 480
webcam = cv2.VideoCapture(0)
webcam.set(3, framewidth)
webcam.set(4, frameheight)


# Start a while loop


    # Reading the video from the
    # webcam in image frames
while True:
    _, img = webcam.read()
    imgHsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('original', img)
    cv2.imshow('rsv Color Space', imgHsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



webcam.release()
cv2.destroyAllWindows()