import Rotate
from collections import deque
import numpy as np
import argparse
import glob
import cv2
from matplotlib import pyplot as plt
import Cntour


def crop ():
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-v", "--video",
		help="path to the (optional) video file")
	ap.add_argument("-b", "--buffer", type=int, default=32,
		help="max buffer size")
	args = vars(ap.parse_args())

	# define the lower and upper boundaries of the "green"
	# ball in the HSV color space
	greenLower = (160,140,100)
	greenUpper = (180,255,255)
	 
	# initialize the list of tracked points, the frame counter,
	# and the coordinate deltas
	pts = deque(maxlen=args["buffer"])
	counter = 0
	(dX, dY) = (0 , 0)
	direction = ""
	k=1
	l=1
	p=''

	# if a video path was not supplied, grab the reference
	# to the webcam
	if not args.get("video", False):
		camera = cv2.VideoCapture(0)
	 
	# otherwise, grab a reference to the video file
	else:
		camera = cv2.VideoCapture(args["video"])


*


	# keep looping

	while True:
		#will start tracking when q is pressed, until then just display the video
		if l ==1:
			while True:
				ret,frame2 = camera.read()
				frame8=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
				rows,cols = frame8.shape
			
				frame2 = cv2.warpAffine(frame2,Rotate.rotate(),(cols,rows))

				cv2.imshow('frame', frame2)
				p=cv2.waitKey(30) & 0xFF
				if p==ord('q'):

					l=0
					break	
	
		if l==0:
			ret,frame0 = camera.read()
			frame8=cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
			rows,cols = frame8.shape
		
		        frame0 = cv2.warpAffine(frame0,Rotate.rotate(),(cols,rows))
		
		
			l=-1
		# grab the current frame
		(grabbed, frame) = camera.read()
		frame8=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rows,cols = frame8.shape
	
		
		frame = cv2.warpAffine(frame,Rotate.rotate(),(cols,rows))
	
	
	

		# if we are viewing a video and we did not grab a frame,
		# then we have reached the end of the video
		if args.get("video") and not grabbed:
			break
		


		# resize the frame, blur it, and convert it to the HSV
		# color space
	
		blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	 
		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, greenLower, greenUpper)
	

		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		cv2.imshow('mask', mask)

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
			if k==1 :
				a = int(M["m10"] / M["m00"])
				b = int(M["m01"] / M["m00"])
				k=0

			# only proceed if the radius meets a minimum size
			if radius > 10:
				#update the list of tracked points
				pts.appendleft(center)
	
		if len(pts)>10 :
			# loop over the set of tracked points
			for i in np.arange(1, len(pts)):
				# if either of the tracked points are None, ignore
				# them
				if pts[i - 1] is None or pts[i] is None:
					continue

				# check to see if enough points have been accumulated in
				# the buffer
				if i == 1 and pts[-10] is not None:
					# compute the difference between the x and y
					# coordinates
					dX = pts[-10][0] - pts[i][0]
					dY = pts[-10][1] - pts[i][1]	
				


		# show the frame to our screen and increment the frame counter
		cv2.imshow("frame", frame)
		key = cv2.waitKey(1) & 0xFF
		counter += 1
	
	# if the 'q' key is pressed, or if the object slows down, loop is exited and the cropped part is displayed
	if (key == ord('q')) or  (len(pts)>24 and np.abs(dX) < 10 and np.abs(dY) < 10):
		c = int(M["m10"] / M["m00"])
	        d = int(M["m01"] / M["m00"])
		#check if it is an image
		if ((d-b)>40) or ((b-d)>40):
			crop_img = frame0[d:b,c:a]
			
			
		else:
			crop_img = frame0[b-50:b,c:a]
			
			crop_img = Cntour.cntour(crop_img)

		
		#cv2.imshow('pic2',crop_img)
		#cv2.imshow('base',frame0)
		#cv2.waitKey(0)
		break
	
	
                

	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()
	return crop_img;


