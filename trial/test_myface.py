# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:10:27 2018

@author: Manyue
"""

import cv2
import numpy as np

faces_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Certis Cisco/OLD/OpenCV-android-sdk/sdk/etc/haarcascades/myfacedetector.xml')

img = cv2.imread('C:/Users/Manyue/Desktop/1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray)

faces = faces_cascade.detectMultiScale(gray,1.3,1)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'ppl',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    print (1)
    

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
    