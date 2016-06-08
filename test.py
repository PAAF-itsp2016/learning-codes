import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
	ret, frame = cap.read()

    # Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
 	lower = np.array([0,0,0])
	upper = np.array([0,250,250])

    # Threshold the HSV image to get only blue colors
	mas = cv2.inRange(hsv, lower, upper)
#	mas2=cv2.inRange(frame, lower, upper)
    # Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mas)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mas)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
        	break

cv2.destroyAllWindows()
