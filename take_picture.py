import numpy as np
import cv2
import time
import os

t=time.asctime(time.localtime(time.time()))


#newpath = '/home/pranjal/iitbombay/extracurriculam activities/ITSP/photo/Session_'+ str(t)
#if not os.path.exists(newpath):
#    os.makedirs(newpath)
cap=cv2.VideoCapture(0)

j=0
while(True):
	ret, frame=cap.read()
	cv2.imshow('telecast',frame)
	k=cv2.waitKey(1) & 0xff
	if k== ord('q'):
		break
	if k== ord('s'):
		newpath = '/home/pranjal/iitbombay/extracurriculam activities/ITSP/photo/session_'+ str(t)
		if not os.path.exists(newpath):
    			os.makedirs(newpath)
		cv2.imwrite(newpath+ '/photo_'+ str(j)+ '.jpg', frame)
		j+=1
	
cap.release()
cv2.destroyAllWindows()
