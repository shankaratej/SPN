# from pygame import mixer
#
# # Starting the mixer
# mixer.init()
#
# # Loading the song
# mixer.music.load("/home/teja/Downloads//Green.m4a")
#
# # Setting the volume
# mixer.music.set_volume(0.7)
#
# # Start playing the song
# mixer.music.play()
#
# #
# # from playsound import playsound
# # playsound("//home//teja//Downloads//Green.m4a", block=False)


import numpy as np
import cv2

def nothing(x):
    pass


cv2.namedWindow("frame")
cv2.createTrackbar('H','frame',0,179,nothing)
cv2.createTrackbar("S",'frame',255,255,nothing)
cv2.createTrackbar("V",'frame',0,255,nothing)

img_hsv= np.zeros((250,500,3),np.uint8)

while True:
    h =cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    img_hsv[:]= (h,s,v)
    img_bgr=cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow("frame",img_bgr)
    key=cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()