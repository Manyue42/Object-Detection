
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
    global img, point1, point2, point_list,img3
    image_list = []
    point_list = []
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:
        point1 = (x,y)
        # cv2.circle(img, point1, 10, (0,255,0), 5)   # green
        print ('1111111111111111111111111')
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        cv2.rectangle(img2, point1, (x,y), (255, 0, 0), 5)   # blue
        # print((x,y))
        cv2.imshow('image', img2)
        print ('222222222222222222222222222222')
    elif event == cv2.EVENT_LBUTTONUP:
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)   # red
        image_list.append(img2)
        img3 = img
        img = img2
        print ('3333333333333333333333')

        print ('4444444444444444444444')
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        img = img3
    # elif event == cv2.EVENT_RBUTTONDBLCLK:
    #     img = img2

def append_data(file_path,category_class, x1, y1, x2, y2):
    global flbase
    with open (file_path, "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow([flbase, category_class, x1, y1, x2, y2])

def load_image(folders_path):
    global img, point_list,i, flbase, keyqqq

    key = cv2.waitKey(100) & 0xFF
    flbase = ''
    i = 1
    point_list = []

    folders = glob.glob(folders_path)
    print(folders)
    # print(1,folders[0])

    object1 = '0'
    object2 = '1'
    object3 = '2'
    file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'
    throw_path = os.path.join('/Users/Manyue/Desktop/Certis Cisco/NEA/test/', 'trainset', 'bin')
    keep_path = os.path.join('/Users/Manyue/Desktop/Certis Cisco/NEA/test/', 'trainset', 'keep')
    for folder in folders:
        path = os.path.join(folder, '*')
        files = glob.glob(path)
        for file in files:
            print('---------------')
            flbase = os.path.basename(file)
            print(flbase)
            img = cv2.imread(file)
            cv2.namedWindow('image')
            # cv2.setMouseCallback(flbase, mouse_position)
            # cv2.setMouseCallback('image',on_mouse)
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
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    print('================')
                    min_x = min(point1[0], point2[0])
                    min_y = min(point1[1], point2[1])
                    width = abs(point1[0] - point2[0])
                    height = abs(point1[1] - point2[1])
                    if width > 30 and height > 30:
                        append_data(file_path, flbase,object1, min_x, min_y, width, height)
                        cv2.putText(img, object1, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                        print(min_x,min_y,width,height)
                        print('q')

                    else:
                        print('!!!!!!!!!!!!!!')

                elif cv2.waitKey(100) & 0xFF == ord('w'):
                    text = str(1)
                    cv2.putText(img, text, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                    min_x = min(point1[0], point2[0])
                    min_y = min(point1[1], point2[1])
                    width = abs(point1[0] - point2[0])
                    height = abs(point1[1] - point2[1])
                    if width > 30 and height > 30:
                        append_data(file_path, flabse,object2, min_x, min_y, width, height)
                        cv2.putText(img, object2, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                        print('w')
                    else:
                        print('!!!!!!!!!!!!!!')

                elif cv2.waitKey(100) & 0xFF == ord('e'):
                    min_x = min(point1[0], point2[0])
                    min_y = min(point1[1], point2[1])
                    width = abs(point1[0] - point2[0])
                    height = abs(point1[1] - point2[1])
                    if width > 30 and height > 30:
                        append_data(file_path, flbase, object3, min_x, min_y, width, height)
                        cv2.putText(img, object3, point1, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 1)
                        print('e')
                    else:
                        print('!!!!!!!!!!!!!!')

            cv2.destroyAllWindows()


imPath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/traindata'
folders_path = os.path.join(imPath,'*')
load_image(folders_path)
file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'