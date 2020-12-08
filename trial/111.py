import cv2
import os
import glob
import numpy as np
import re
import csv
import copy

# drawing = False  # if start drawing
# mode = True  # True: drawing rectangle，False：drawing circle
# start = (-1, -1)
# points = []

global fp
fp = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/' # folder path


def on_mouse(event, x, y, flags, param):
    global img, point1, point2 # , start, drawing, mode
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        cv2.circle(img, point1, 10, (0,255,0), 5)   # green
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x,y), (255, 0, 0), 5)   # blue
        # print((x,y))
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)   # red
        img = img2
        min_x = min(point1[0],point2[0])
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        coor =  min_x, min_y,width,height
        print (coor)
        point_list.append((min_x,min_y,width,height))


def main():
    global img, point_list
    point_list = []
    img = cv2.imread('/Users/Manyue/Desktop/1.jpg')
    cv2.namedWindow('image')
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', on_mouse)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()