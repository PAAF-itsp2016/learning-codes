# import the necessary packages
from collections import deque
import numpy as np
import argparse
import glob
import cv2
from matplotlib import pyplot as plt



def cntour (crop_img):


	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
	ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
	args = vars(ap.parse_args())
	# define the lower and upper boundaries of the "green"
	# ball in the HSV color space, then initialize the
	# list of tracked points
	greenLower = (0, 0, 100)
	greenUpper = (255, 100, 255)
	pts = deque(maxlen=args["buffer"])

	# resize the frame, blur it, and convert it to the HSV
	# color space
	
	blurred = cv2.GaussianBlur(crop_img, (11, 11), 0)
	hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)[-2]
	if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			e = int(M["m10"] / M["m00"])
			f = int(M["m01"] / M["m00"])
			crop_img2 = crop_img[0:f+3,0:10000000]
			#cv2.imwrite('pic3.jpg',crop_img2)

			return crop_img2;
