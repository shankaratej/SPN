# Python code for Multiple Color Detection
import img as img
import numpy as np
import cv2

# Capturing video through webcam
frameWidth = 640
frameHeight = 480
webcam = cv2.VideoCapture(0)
webcam.set(3, frameWidth)
webcam.set(4, frameHeight)


# Start a while loop
def empty(a):
    pass

#
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE min",'HSV',0,179,empty)
cv2.createTrackbar("HUE max",'HSV',179,179,empty)
cv2.createTrackbar("SAT min",'HSV',0,255,empty)
cv2.createTrackbar("SAT max",'HSV',255,255,empty)
cv2.createTrackbar("VALUE min",'HSV',0,255,empty)
cv2.createTrackbar("VALUE max",'HSV',255,255,empty)

    # Reading the video from the
    # webcam in image frames
while True:

    _, img = webcam.read()
    imgHsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("HUE MIN", "HSV")
    # h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    # s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    # s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    # v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    # v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    # lower= np.array([h_min, s_min, v_min])
    # upper=np.array([h_max,s_max,v_max])
    # mask=cv2.inRange([imgHsv,lower,upper])
    # result= cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('original', img)
    cv2.imshow('HSV Color Space', imgHsv)
    # cv2.imshow(' Mask', mask)
    # cv2.imshow('Result', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



webcam.release()
cv2.destroyAllWindows()