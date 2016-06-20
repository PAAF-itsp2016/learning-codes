# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from espeak import espeak
import time
rot=0
def rotate(frame):

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video",
		help="path to the (optional) video file")
	ap.add_argument("-b", "--buffer", type=int, default=32,
		help="max buffer size")
	args = vars(ap.parse_args())
	
	# define the lower and upper boundaries of the "green"
	# ball in the HSV color space
	lower = (160,140,100)
	upper = (180,255,255)
	 
	# initialize the list of tracked points, 
	# and the coordinate deltas
	pts = deque(maxlen=args["buffer"])
	(dX, dY) = (0, 0)

	
	# if a video path was not supplied, grab the reference
	# to the webcam
	if not args.get("video", False):
		camera = cv2.VideoCapture(0)
	 
	# otherwise, grab a reference to the video file
	else:
		camera = cv2.VideoCapture(args["video"])
	
	
	espeak.synth("Hi, I am Jarvis. Your life, or the bottom left corner of your page. He  he  hee hee heeeee..")
	time.sleep(5)
		
	# keep looping

	while True:
			
		
		# grab the current frame
		(grabbed, frame) = camera.read()
	
		# if we are viewing a video and we did not grab a frame,
		# then we have reached the end of the video
		if args.get("video") and not grabbed:
			break		

		# resize the frame, blur it, and convert it to the HSV
		# color space
		frame = imutils.resize(frame, width=600)
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	 
		# construct a mask for required colour, then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, lower, upper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
	
		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None
		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
	
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	
			# only proceed if the radius meets a minimum size
			if radius > 10:
				# update the list of tracked points
				pts.appendleft(center)
		
		if len(pts)>10 :
			if pts[i] is not None:

				if pts[-10] is not None:
					# compute the difference between the x and y
					# coordinates
					dX = pts[-10][0] - pts[1][0]
					dY = pts[-10][1] - pts[1][1]	
	
		
		key = cv2.waitKey(1) & 0xFF

	
		# if the 'q' key is pressed, or if the object slows down, the variable is updated and the function ends
		if ((key == ord('q')) or  (len(pts)>30 and np.abs(dX) < 25 and np.abs(dY) < 25)):
			c = int(M["m10"] / M["m00"])
		        d = int(M["m01"] / M["m00"])
			if c < 300.0 and d < 225.0:		#the values are dependant upon the pixels of the frame
				rot= 1;
				return cv2.getRotationMatrix2D((cols/2,rows/2),90,1);
				
			elif c < 300.0 and d >= 225.0:
				rot= 2;
				return cv2.getRotationMatrix2D((cols/2,rows/2),0,1);
	
			elif c >= 300.0 and d < 225.0:
				rot=3;
				return cv2.getRotationMatrix2D((cols/2,rows/2),180,1);

			elif c >= 300.0 and d >= 225.0:
				rot=4;
				return cv2.getRotationMatrix2D((cols/2,rows/2),270,1);
			# cleanup the camera and close any open windows
			camera.release()
			return;
	
