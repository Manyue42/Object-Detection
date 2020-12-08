import cv2
import numpy as np
import copy

global img
global point1, point2
drawing = False
mode = True
start = (-1,-1)


def on_mouse(event, x, y, flags, param):
    global img, point1, point2, drawing, mode
    print(1)
    img2 = copy.deepcopy(img)
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        drawing = True
        point1 = x,y
        # cv2.circle(img, point1, 10, (0,255,0), -1)
        # cv2.imshow('image', img)
        # mouse is moving and left click and drag
    # elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
    #     cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
    #     cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        print (drawing)
        if drawing == True:
            if mode == True:
                cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
                print ('aaaaaaaaaaaaaaa')
                cv2.imshow('image', img2)
            else:
                cv2.circle(img, (x,y), 5, (0,0,255), -1)
    elif event ==cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            point2 = (x, y)
            cv2.rectangle(img2, point1, point2, (0,0,255), 5)
            cv2.imshow('image', img)
            img = img2
            min_x = min(point1[0],point2[0])
            min_y = min(point1[1],point2[1])
            width = abs(point1[0] - point2[0])
            height = abs(point1[1] -point2[1])
            coor =  min_x, min_y,width,height
            print (coor)
            point_list.append((min_x,min_y,width,height))
        else:
            cv2.circle(img, (x,y), 5, (0,0,255), -1)

    print(2)
    # elif event == cv2.EVENT_LBUTTONUP:         #左键释放
    #     point2 = (x,y)
    #     cv2.rectangle(img2, point1, point2, (0,0,255), 5)
    #     cv2.imshow('image', img2)
    #     min_x = min(point1[0],point2[0])
    #     min_y = min(point1[1],point2[1])
    #     width = abs(point1[0] - point2[0])
    #     height = abs(point1[1] -point2[1])
    #     coor =  min_x, min_y,width,height
    #     print (coor)
    #     point_list.append((min_x,min_y,width,height))

def main():
    global img, point_list
    point_list = []

    img = cv2.imread('/Users/Manyue/Desktop/1.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    print(3)
    cv2.imshow('image', img)
    print(4)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

