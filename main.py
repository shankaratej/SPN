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
    hsv_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx=int(width/2)
    cy=int(height/2)


    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
   # cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pixel_center= hsv_frame[cy,cx]

    hue_value=pixel_center[0]
    color="UNDEFINED"

    if hue_value < 5:
        color= "RED"
    elif hue_value<22:
        color="ORANGE"
    elif hue_value< 33:
        color="YELLOW"
    elif hue_value<78:
        color="GREEN"
    elif hue_value<131:
        color="BLUE"
    elif hue_value<167:
        color="VIOLET"
    else:
        color="RED"

    pixel_center_bgr=hsv_frame[cy,cx]
    cv2.putText(frame, color,(10,50), 0,1,(255,0,0),2)
    cv2.circle(frame, (cx,cy), 5, (255,0,0), 3)
    cv2.imshow('Frame',frame)
    key= cv2.waitKey(1)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()

