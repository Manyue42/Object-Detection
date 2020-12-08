import cv2
import os
import glob
import numpy as np
import re
import csv

import copy
# global img2
# global point1, point2
drawing = False
mode = True
start = (-1,-1)
points =[]


def on_mouse(event, x, y, flags, param):
    print(1)
    global img, point1, point2, start, drawing, mode
    img2 = copy.copy(img)

    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        print('~~~~~~~~~~')
        print(x,y)
        point1 = (x,y)
        cv2.circle(img, point1, 10, (0,255,0), 5)
        # cv2.imshow('image', img2)
        # mouse is moving and left click and drag
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        print('@@@@@@@@@@')

        cv2.rectangle(img2, point1, (x,y), (255, 0, 0), 5)

        # img2 = copy.deepcopy(img)
        # cv2.rectangle(img, point1, (x,y), (255,0,0), 5)

        print((x,y))
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        print('##########')
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5)
        # img = img2
        min_x = min(point1[0],point2[0])
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        coor =  min_x, min_y,width,height
        print (coor)
        point_list.append((min_x,min_y,width,height))
    print(2)

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     drawing = True
    #     point1 = (x,y)

        # file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'
        # category_class = '0'
        # with open(file_path, "a", newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([file_path, category_class, min_x, min_y,width,height])

# def append_data(file_path,catogory_class):
#     with open (file_path, "a",newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow([file_path, category_class)

#
def load_image(fold_path):
    global img, point_list
    point_list = []

    folders = glob.glob(folders_path)
    print(folders)
    # print(1,folders[0])

    object1 = '0'
    object2 = '1'
    object3 = '2'
    file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'
    for file in folders:
        print('---------------')
        flbase = os.path.basename(file)
        print(flbase)
        img = cv2.imread(file)
        cv2.namedWindow(flbase)
        cv2.setMouseCallback(flbase, mouse_position)
        while 1:
            cv2.imshow(flbase, img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                x = point_list[0][0]
                y = point_list[0][1]
                width = point_list[1][0] - point_list[0][0]
                high = point_list[1][1] - point_list[0][1]
                if width > 30 and high > 30:
                    append_data(file_path, object1, x, y, width, high)
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
                    print('e')
                else:
                    print('!!!!!!!!!!!!!!')
                break

        point_list = []
        cv2.destroyAllWindows()


def check_overlap():
    point





def main():
    global img, point_list
    point_list = []

    # imPath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/'
    # folders_path = os.path.join(imPath, '*')
    # load_image(folders_path)
    # file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'


    img = cv2.imread('/Users/Manyue/Desktop/1.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
