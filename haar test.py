import cv2
import numpy as np


trap_body_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Haar Test/TEST_old/cascade_body.xml')
trap_cover_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Haar Test/TEST_old/cascade_cover.xml')
trap_filter_cascade = cv2.CascadeClassifier('C:/Users/Manyue/Desktop/Haar Test/TEST_old/cascade_filter.xml')



img = cv2.imread('C:/Users/Manyue/Desktop/000002309.jpg')
# img = cv2.imread('C:/Users/Manyue/Desktop/color/neg/2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1.2 indicate the searching box will increase size in 20% every time
# 12 minimum neighbors
trapbody = trap_body_cascade.detectMultiScale(gray, 1.3, 11)
trapcover = trap_cover_cascade.detectMultiScale(gray, 1.3, 11)
trapfilter = trap_filter_cascade.detectMultiScale(gray, 1.2, 11)

for (x,y,w,h) in trapbody:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
for (x,y,w,h) in trapcover:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
for (x,y,w,h) in trapfilter:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow('img', img)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()


