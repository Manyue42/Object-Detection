# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:45:40 2018

@author: Manyue
"""
import cv2
import numpy as np

# face_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Certis Cisco/OLD/OpenCV-android-sdk/sdk/etc/haarcascades/haarcascade_frontalface_default.xml')

# eye_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Certis Cisco/OLD/OpenCV-android-sdk/sdk/etc/haarcascades/haarcascade_eye.xml')

# watch_cascade = cv2.CascadeClassifier('watch-cascade.xml')


# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#faces = face_cascade.detectMultiScale(gray)
# watches = watch_cascade.detectMultiScale(gray, 1.2, 5)


# 1.2 indicates that every time the searching box will increase size in 20%

# for (x,y,w,h) in watches:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img,'ppl',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
#     print (1)
cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
    
    