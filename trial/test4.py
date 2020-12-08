import cv2
import os
import glob
import numpy as np
import re
import csv



global img, point1, point2, point_list, flbase,i, img3
state = 1
flbase = ''
point_list = []
i = 1

def mouse_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        print(x, y)
        point_list.append((x, y))

def on_mouse(event, x, y, flags, param):
    global img, point1, point2, point_list,img3,text
    point_list = []
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        # cv2.circle(img, point1, 10, (0,255,0), 5)   # green
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x,y), (255, 0, 0), 5)   # blue
        cv2.imshow('image', img2)
        # print ('222222222222222222222222222222')
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)   # red
        img3 = img
        img = img2
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        img = img3

def append_data(file_path,category_class, x1, y1, x2, y2):
    global flbase
    with open (file_path, "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow([flbase, category_class, x1, y1, x2, y2])

def load_image(folders_path):
    global img, point_list,flbase,action
    point_list = []

    folders = glob.glob(folders_path)
    print(folders)
    # print(1,folders[0])

    object1 = '0'  # cap
    object2 = '1'  # bottle
    object3 = '2'  # white board
    file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'
    throw_path = os.path.join('/Users/Manyue/Desktop/Certis Cisco/NEA/test/', 'trainset', 'bin')
    print(throw_path)
    keep_path = os.path.join('/Users/Manyue/Desktop/Certis Cisco/NEA/test/', 'trainset', 'keep')
    for file in folders:
        print('---------------')
        flbase = os.path.basename(file)
        print(flbase)
        img = cv2.imread(file)
        cv2.namedWindow('image')
        # cv2.setMouseCallback(flbase, mouse_position)
        while 1:
            cv2.imshow('image', img)
            cv2.setMouseCallback('image', on_mouse)
            if cv2.waitKey(100) & 0xFF == ord('p'):
                os.rename(file, os.path.join(throw_path, flbase))
                print('Throw!!!!!!!!!!!!!')
                break
            if cv2.waitKey(100) & 0xFF == ord('n'):
                os.rename(file, os.path.join(keep_path, flbase))
                print('keeppppppppppppppp')
                break
            # if cv2.waitKey(100) & 0xFF == ord('q'):
            if cv2.EVENT_LBUTTONDBLCLK:
                print('================')
                min_x = min(point1[0], point2[0])
                min_y = min(point1[1], point2[1])
                width = abs(point1[0] - point2[0])
                height = abs(point1[1] - point2[1])
                if width > 30 and height > 30:
                    append_data(file_path, object1, min_x, min_y, width, height)
                    text = str(0)  # bottle
                    cv2.putText(img, object1, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255,0), 1)
                    # print(min_x, min_y, width, height)
                    print('q')

                else:
                    print('!!!!!!!!!!!!!!')

            elif cv2.waitKey(100) & 0xFF == ord('w'):
                min_x = min(point1[0], point2[0])
                min_y = min(point1[1], point2[1])
                width = abs(point1[0] - point2[0])
                height = abs(point1[1] - point2[1])
                if width > 30 and height > 30:
                    append_data(file_path, object2, min_x, min_y, width, height)
                    cv2.putText(img, object2, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255,0), 1)
                    print('w')
                else:
                    print('!!!!!!!!!!!!!!')

            elif cv2.waitKey(100) & 0xFF == ord('e'):
                min_x = min(point1[0], point2[0])
                min_y = min(point1[1], point2[1])
                width = abs(point1[0] - point2[0])
                height = abs(point1[1] - point2[1])
                if width > 30 and height > 30:
                    append_data(file_path, object3, min_x, min_y, width, height)
                    text = str(2)  # white board
                    cv2.putText(img, object3, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255,0), 1)
                    print('e')
                else:
                    print('!!!!!!!!!!!!!!')

        cv2.destroyAllWindows()

imPath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/traindata'
folders_path = os.path.join(imPath, '*')
load_image(folders_path)
file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'