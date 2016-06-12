import cv2
import Image
import numpy as np

img = cv2.imread('index2.jpg')
ball = img[235:280, 280:330]
img[65:110, 170:220] = ball

cv2.imshow('new', img)
cv2.waitKey(0)
