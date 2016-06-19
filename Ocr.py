import Image
import cv2
import numpy as np 
import pytesseract

def ocr(img):
	img = cv2.imread('index1.jpg')
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	a = np.array([0,0,140])
	b = np.array([180,100,255])
	
	mask = cv2.inRange(hsv, a, b)
	cv2.imshow('before', mask)
	#mask1 = img
	mask = cv2.dilate(mask, None, iterations=2)	
	mask = cv2.erode(mask, None, iterations=2)
	#mask1 = cv2.fastNlMeansDenoising(mask, mask1, 200)
	
	cv2.imshow('after', mask)
	cv2.imshow('image', img)
	cv2.imwrite('test.jpg', mask)
	s= pytesseract.image_to_string(Image.open('test.jpg'))
	os.remove('test.jpg')
	return s
