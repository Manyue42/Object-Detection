import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = ['train']
classes = ["trap body", "trap filter", "trap cover"]
dir_path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/NEA_rawData_10/'
throw_path = os.path.join('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/NEA_rawData_10/','ImageSets','bin')

def convert_annotation(image_id):
    in_file = open(dir_path + 'Annotations/%s.xml' % (image_id))  # （如果使用的不是VOC而是自设置数据集名字，则这里需要修改）
    out_file = open(dir_path + 'labels/%s.txt' % (image_id), 'w')  # （同上）
    # element tree, wrap an element structure, and convert it from and to XML
    tree = ET.parse(in_file)
    # Returns the root element for this tree
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    filename = root.find('filename').text
    path = root.find('path').text
    path = path.replace('\\','/')


    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            os.rename(path, os.path.join(throw_path, filename))
            break
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        # #  ----------------------------- output file name, obejct class, x/w, y/h, cx/w, cy/h
        # bb = convert((w, h), b)
        # out_file.write(filename + " " + cls + " " + " ".join([str(a) for a in bb]) + '\n')
        #
        #
        # # #  ----------------------------- output file name, object class, xmin, xmin, xmax, ymin, ymax
        # out_file.write(filename + " " + cls + " " + " ".join([str(a) for a in b]) + '\n')

        # #  ----------------------------- output obj class name, xmin, ymax, width, height
        width = abs(b[0] - b[1])
        height = abs(b[2] - b[3])
        out_file.write(filename + " " + cls + " " + str(b[0]) + " " + str(b[3]) + " " + str(width) + " " + str(height) + "\n")


def getFileName(path,fileList):
    if os.path.isfile(path):
        fileList.append(path)
        print('file')
    elif os.path.isdir(path):
        print('dir')
        for s in os.listdir(path):
            newDir = os.path.join(path, s)
            getFileName(newDir, fileList)
    return fileList
path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/NEA_rawData_10/Annotations/'
list = getFileName(path, [])

fo = open("C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/NEA_rawData_10/ImageSets/Main/train.txt","w")
for i in list:
    print(i)
    name = os.path.splitext(os.path.basename(i))[0]
    fo.write(name + '\n')
fo.close()



for image_set in sets:
    if not os.path.exists(dir_path +'labels/'):
        os.makedirs(dir_path + 'labels/')
    image_ids = open( dir_path + 'ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        # list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n' % (wd, year, image_id))
        # list_file.write('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/JPEGImages/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()


