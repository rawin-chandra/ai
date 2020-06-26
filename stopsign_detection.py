'''
credit:
https://www.geeksforgeeks.org/detect-an-object-with-opencv-python

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html

create by T. Rawin (T. S)
if you use webcam you should change VideoCapture(0) to VideoCapture(1)

and download stop_data.xml to the same directory as this file
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('stop_data.xml')

while(True):
   
    ret, frame = cap.read()    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    found = face.detectMultiScale(gray,minSize =(20, 20))
    amount_found = len(found)
    if amount_found != 0:
		for (x, y, width, height) in found:
			cv2.rectangle(frame, (x, y),(x + height, y + width),(0, 255, 0), 5)
			
    cv2.imshow('frame',frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
