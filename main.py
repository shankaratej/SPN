# Python code for Multiple Color Detection


import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Start a while loop


    # Reading the video from the
    # webcam in image frames
while True:
    _, frame = webcam.read()
    height, width, _ = frame.shape

    cx=int(width/2)
    cy=int(height/2)


    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
   # cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pixel_center= frame[cy,cx]
    print(pixel_center)
    cv2.circle(frame, (cx,cy), 5, (255,0,0), 3)
    cv2.imshow('Frame',frame)
    key= cv2.waitKey(1)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()

