import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import cv2
import glob
import numpy as np
import re
import csv

# dir_path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/'
dir_path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA-dataset/'


# path of saving training images
# save_path = os.path.join('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/trainset/trainsets/')
save_path = os.path.join('C:/Users/Manyue/Desktop/Certis Cisco/NEA-dataset/trainset/')


# output text file path
# out_file = open(dir_path + 'trainset/train.txt', 'w')


# output text file for haar
# haar_out1 = open(save_path + 'trap body/pos.txt', 'w')
# haar_out2 = open(save_path + 'trap filter/pos.txt', 'w')
# haar_out3 = open(save_path + 'trap cover/pos.txt', 'w')

# haar_out1 = open(save_path + 'trap_body/pos.txt', 'w')
# haar_out2 = open(save_path + 'trap_filter/pos.txt', 'w')
# haar_out3 = open(save_path + 'trap_cover/pos.txt', 'w')



# folders_path = os.path.join(dir_path, 'traindata', '*')
folders_path = os.path.join(dir_path, 'rawData', '*')
folders = glob.glob(folders_path)

true_classes = ['trap body', 'trap filter', 'trap cover']
false_classes = ['in trap body', 'in trap filter', 'in trap cover']
other_classes = ['bottle', 'ttin trap filter']


for folder in folders:
    path1 = os.path.join(folder,'Annotations', '*')
    files = glob.glob(path1)
    for file in files:
        tree = ET.parse(file)
        # Returns the root element for this tree
        root = tree.getroot()
        size = root.find('size')
        img_w = int(size.find('width').text)
        img_h = int(size.find('height').text)
        filename = root.find('filename').text
        path = root.find('path').text
        path = path.replace('\\', '/')
        label_path = file.replace('Annotations', 'labels').replace('.xml', '.txt').replace('\\', '/')
        xml_out = open(label_path, 'w')
        # print(file)


        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in true_classes:
                continue
            cls_id = true_classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            width = abs(b[0] - b[1])
            height = abs(b[2] - b[3])
            img_path = file.replace("Annotations", "JPEGImage").replace('xml', 'jpg').replace('\\', '/')
            # img_path = img_path.replace('xml', 'jpg')
            # img_path = img_path.replace('\\', '/')

            # img_name = os.path.basename(img_path)
            b0 = int(b[0])
            b1 = int(b[1])
            b2 = int(b[2])
            b3 = int(b[3])
            obj_w = int(width)
            obj_h = int(height)

            # dw = 1./w
            # dh = 1./h
            # x = (b[0] + b[1]) / 2.0
            # y = (b[2] + b[3]) / 2.0
            # x = x * dw
            # w = width * dw
            # y = y * dh
            # h = height * dh

            x = ((b[0] + b[1]) / 2.0) / img_w
            y = ((b[2] + b[3]) / 2.0) / img_h
            w = width / img_w
            h = height / img_h





# put if before calculation, saving time
# put cls_id before, void reading twice
# using try/exception
# close the file everytime open it


            # out_file.write(filename + " " + cls + " " + " ".join([str(a) for a in b]) + '\n')

            # crop image and save in three different folders, create pos.txt for each object
            img = cv2.imread(img_path)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            cropImg = img[b2:b2+h,b0:b0+w]
            cropImg = cv2.resize(cropImg, (50,50))
            #
            if cls == true_classes[0]:
                cv2.imwrite(save_path + 'trap_body/'+ filename, cropImg)
                # haar_out1.write(filename + " 1 0 0 50 50 " + '\n')
                haar_out1.write(filename + " 1 0 0 " + str(obj_w) + " " + str(obj_h) + '\n')
            if cls == true_classes[1]:
                cv2.imwrite(save_path + 'trap_filter/'+ filename, cropImg)
                # haar_out2.write(filename + " 1 0 0 50 50 " + '\n')
                haar_out2.write(filename + " 1 0 0 " + str(obj_w) + " " + str(obj_h) + '\n')

            if cls == true_classes[2]:
                cv2.imwrite(save_path + 'trap_cover/'+ filename, cropImg)
                # haar_out3.write(filename + " 1 0 0 50 50 " + '\n')
                haar_out3.write(filename + " 1 0 0 " + str(obj_w) + " " + str(obj_h) + '\n')




            xml_out.write(str(cls_id) + " " + str(x) + " " + str(y) + " " +
                          str(w) + " " + str(h) + '\n')

        xml_out.close()