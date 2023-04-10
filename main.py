# Python code for Multiple Color Detection


import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)


# Start a while loop


    # Reading the video from the
    # webcam in image frames
while True:
    _, imageFrame = webcam.read()
    heigth, width, _ = webcam.shape

    cx=int(width/2)
    cy=heigth/2


    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    cv2.imshow("Frame", imageFrame)
    key= cv2.waitKey(1)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()

