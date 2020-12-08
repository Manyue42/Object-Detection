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



def append_data(file_path,category_class, x1, y1, x2, y2):
    with open (file_path, "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerow([file_path, category_class, x1, y1, x2, y2])


def load_image(folders_path):
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


print('3')

imPath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/'
folders_path = os.path.join(imPath, '*')
load_image(folders_path)
file_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/NAME.csv'

