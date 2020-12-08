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


dir_path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/'
# path of saving training images
save_path = os.path.join('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/trainset/trainsets')

# output text file path
out_file = open(dir_path + 'trainset/train.txt', 'w')


folders_path = os.path.join(dir_path, 'traindata', '*')
folders = glob.glob(folders_path)


true_classes = ['trap body', 'trap filter', 'trap cover']
false_classes = ['in trap body', 'in trap filter', 'in trap cover']
other_classes = ['bottle', 'ttin trap filter']

file_list = []
for folder in folders:
    path = os.path.join(folder,'Annotations', '*')
    files = glob.glob(path)
    for file in files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        file_list.append(file_name)
f_list = file_list
print (f_list)


folders_path = os.path.join(dir_path, 'traindata/NEA_rawData_10', '*')
folders = glob.glob(folders_path)

for folfer in folders:
    path2 = os.path.join(folder,'JPEGImage','*')
    files2 = glob.glob(path2)
    for file in files2:
        f_name = os.path.splitext(os.path.basename(file))[0]
        new_name = f_name + '.jpg'
        if f_name not in f_list:
            os.rename(file, os.path.join(save_path,new_name))