import numpy as np
import cv2
from time import sleep
import sys
sys.path.append("./data")

name=input('first letter of your name')

getready=['ready for fist right hand','ready for stop right hand','ready for peace right hand','ready for thumbsup right hand']
capture=["fist right hand...",'stop right hand...','peace right hand...', 'thumbsup,right hand...']
f_names=['data/fist/fist'+name+'R(%d).jpg','data/stop/stop'+name+'R(%d).jpg','data/peace/peace'+name+'R(%d).jpg','data/thumbs/thumbs'+name+'R(%d).jpg']

cap = cv2.VideoCapture(0)
for j in range(4):
	print(getready[j])
	for i in range(10):
		print(capture[j],i+1)
		while True:
			ret, frame = cap.read()
			frame = cv2.flip(frame, 3)
			roiR = frame[100:300, 400:600]
			gray = cv2.cvtColor(roiR, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(5,5),2)   
			th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
			ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			cv2.imshow('frame',frame)
			cv2.imshow('roiR',res)
			if cv2.waitKey(1) & 0xFF == ord('q'):
                        	break
		x=f_names[j] % i
		cv2.imwrite(x, res)
cap.release()
cv2.destroyAllWindows()

getready=['ready for fist left hand','ready for stop left hand','ready for left right hand','ready for thumbsup left hand']
capture=["fist left hand...",'stop left hand...','peace left hand...', 'thumbsup left hand...']
f_names=['data/fist/fist'+name+'L(%d).jpg','data/stop/stop'+name+'L(%d).jpg','data/peace/peace'+name+'L(%d).jpg','data/thumbs/thumbs'+name+'L(%d).jpg']
cap = cv2.VideoCapture(0)
for j in range(4):
	print(getready[j])
	for i in range(10):
		print(capture[j],i+1)
		while True:
			ret, frame = cap.read()
			frame = cv2.flip(frame, 3)
			roiL = frame[100:300, 50:250]
			gray = cv2.cvtColor(roiL, cv2.COLOR_BGR2GRAY)
			blur = cv2.GaussianBlur(gray,(5,5),2)
			th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
			ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			cv2.imshow('frame',frame)
			cv2.imshow('roiL',res)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		x=f_names[j] % i
		cv2.imwrite(x, res)
	
cap.release()
cv2.destroyAllWindows()
