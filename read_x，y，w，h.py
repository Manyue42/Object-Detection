import cv2
import os
import glob
import numpy as py
import re

imPath = 'C:/Users/Manyue/Desktop/Certis Cisco/LPR_Test/'
def mouse_position(event, x, y, flags, param):
    # EVENT_LBUTTONDBLCLK event is double click left mouse
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # draw a circle on the image us blue
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
        print(x, y)
        point_list.append((x, y))


def load_image(folders_path):
    global img, point_list
    point_list = []

    folders = glob.glob(folders_path)
    print(1,folders)

    # store path
    #path_1_line = os.path.join('/Users/weiwenju/Certis/LPR/', 'trainset', '1-line')
   # path_2_line = os.path.join('/Users/weiwenju/Certis/LPR/', 'trainset', '2-line')
   # path_throw = os.path.join('/Users/weiwenju/Certis/LPR/', 'trainset', 'throw')
    
    path_1_line = os.path.join(imPath,'trainset','1-line')
    path_2_line = os.path.join(imPath,'trainset','2-line')
    path_throw = os.path.join(imPath,'trainset','throw')

    for folder in folders:

        # use os.path.join to combine different component to a complete path
        path = os.path.join(folder, '*.jpg')

        # use glob to find the files who meet the path and open all images in this path
        files = glob.glob(path)
        print('f',files)

        for file in files:
            print('---------------')
            # basename()   return the image name
            flbase = os.path.basename(file)  #returns names of images
            image = re.search('OCR_.*?-(.*?)-',flbase).group(1) #group the matched images 

            # read the image
            img = cv2.imread(file) 
            print (file)
            # name the handle window
            cv2.namedWindow(image)
            print(image)
            #  handle mouse events in OpenCV
            cv2.setMouseCallback(image, mouse_position)
            while 1:
                cv2.imshow(image, img)

                # wait the keyboard input if press 'q' store in 1-line else store in 2-line. cv2.waitKey(200) & 0xFF
                # just change the binary representation
                if cv2.waitKey(100) & 0xFF == ord('q'):

                    # record x,y,width,high
                    x = point_list[0][0]
                    y = point_list[0][1]
                    width = point_list[1][0] - point_list[0][0]
                    high = point_list[1][1] - point_list[0][1]

                    if width > 30 and high > 30:
                            # change the image name and store
                            os.rename(file, os.path.join(path_1_line, image + '_' + 's' + '_' + '1' + '_' + str(x) + '_'
                                                         + str(y) + '_' + str(width) + '_' + str(high) + '_' + '.jpg'))
                            print('q')
                    else:
                        print('!!!!!!!!!!!!!!')

                    break

                elif cv2.waitKey(100) & 0xFF == ord('e'):
                    x = point_list[0][0]
                    y = point_list[0][1]
                    width = point_list[1][0] - point_list[0][0]
                    high = point_list[1][1] - point_list[0][1]

                    if width > 30 and high > 30:
                        os.rename(file, os.path.join(path_2_line, image + '_' + 'd' +  '_' + '1' + '_' + str(x) + '_'
                                                 + str(y) + '_' + str(width) + '_' + str(high) + '_' + '.jpg'))
                        print('e')

                    else:
                        print('!!!!!!!!!!!!!!')
                    break

                elif cv2.waitKey(100) & 0xFF == ord('t'):
                    try:
                        os.rename(file, os.path.join(path_throw, image + '.jpg'))
                        print('t')
                    except Exception as e :
                        print(e)

                    break

            point_list = []
            cv2.destroyAllWindows()
    print('3')


#path_folders = os.path.join('/Users/weiwenju/Certis/LPR/','traindata','*')
path_folders = os.path.join(imPath,'traindata','*')

print(2,path_folders)
load_image(path_folders)

