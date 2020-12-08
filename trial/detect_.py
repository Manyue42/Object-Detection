# -*- coding: utf-8 -*-
"""
Created on Thu May 31 17:11:17 2018

@author: Manyue
"""

import cv2
import os
import glob
import numpy as np
import re
import csv



def mouse_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        print(x, y)
        point_list.append((x, y))


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


def append_data(file_path,category_class, x1, y1, x2, y2):
    global i
    with open (file_path, "a",newline='') as f:
        writer = csv.writer(f)
        img_name = '0000'+ str(i) + '.png'
        writer.writerow([img_name, category_class, x1, y1, x2, y2])
        i+=1

# def rename(path):




def load_image(folders_path):
    global img, point_list,i
    i = 1
    point_list = []

    folders = glob.glob(folders_path)
    print(folders)
    # print(1,folders[0])

    object1 = '0'
    object2 = '1'
    object3 = '2'
    file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'
    new_path = os.path.join( '/Users/Manyue/Desktop/Certis Cisco/NEA/test/', 'trainset')
    for folder in folders:
        path = os.path.join(folder, '*')
        files = glob.glob(path)


        for file in files:
            print('---------------')
            flbase = os.path.basename(file)
            print(flbase)
            img = cv2.imread(file)
            cv2.namedWindow(flbase)
            cv2.setMouseCallback(flbase, mouse_position)
            # cv2.setMouseCallback(flbase,on_mouse)
            while 1:
                cv2.imshow(flbase, img)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    x = point_list[0][0]
                    y = point_list[0][1]
                    width = point_list[1][0] - point_list[0][0]
                    high = point_list[1][1] - point_list[0][1]
                    if width > 30 and high > 30:
                        append_data(file_path, object1, x, y, width, high)
                        # os.rename(file, os.path.join(new_path, str(i) +'.jpg'))

                       # os.rename(file, os.path.join(path_1_line, image + '_' + 's' + '_' + '1' + '_' + str(x) + '_'
                       #                              + str(y) + '_' + str(width) + '_' + str(high) + '_' + '.jpg'))
                        print(str(i))
                        print('q')
                    else:
                        print('!!!!!!!!!!!!!!')
                    break
                elif cv2.waitKey(100) & 0xFF == ord('w'):
                    y = point_list[0][1]
                    x = point_list[0][0]
                    width = point_list[1][0] - point_list[0][0]
                    high = point_list[1][1] - point_list[0][1]
                    if width > 30 and high > 30:
                        append_data(file_path, object2, x, y, width, high)
                        # os.rename(file, os.path.join(new_path, new_path+ str(i)+'.jpg'))

                        print('w')
                    else:
                        print('!!!!!!!!!!!!!!')
                    break
                elif cv2.waitKey(100) & 0xFF == ord('e'):
                    x = point_list[0][0]
                    y = point_list[0][1]
                    width = point_list[1][0] - point_list[0][0]
                    high = point_list[1][1] - point_list[0][1]
                    if width > 30 and high > 30:
                        append_data(file_path, object3, x, y, width, high)
                        # os.rename(file, os.path.join(new_path, new_path+ str(i)+'.jpg'))

                        print('e')
                    else:
                        print('!!!!!!!!!!!!!!')
                    break


            point_list = []
            cv2.destroyAllWindows()
    print('3')


imPath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/'
folders_path = os.path.join(imPath,'*')
load_image(folders_path)
file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'