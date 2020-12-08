import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# this script is for converting xml file into text file
# it is specially used for yolo2

sets = [('2007','train')]
classes = ["cap", "bottle", "board"]


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(year, image_id):
    in_file = open('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC%s/Annotations/%s.xml' % (year, image_id))  # （如果使用的不是VOC而是自设置数据集名字，则这里需要修改）
    out_file = open('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC%s/labels/%s.txt' % (year, image_id), 'w')  # （同上）
    # in_file = open('\Users\Manyue\Desktop\Certis Cisco\NEA\VOCdevkit\VOC%s\Annotations\%s.xml' % (year, image_id))
    # out_file = open('\Users\Manyue\Desktop\Certis Cisco\NEA\VOCdevkit\VOC%s\labels\%s.txt' % (year, image_id), 'w')
    # element tree, wrap an element structure, and convert it from and to XML
    tree = ET.parse(in_file)
    # Returns the root element for this tree
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# wd = os.getcwd()

for year, image_set in sets:
    if not os.path.exists('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/labels/'):
        os.makedirs('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/labels/')
    image_ids = open('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC%s/ImageSets/Main/%s.txt' % (year,image_set)).read().strip().split()
    # image_ids = ['000001', '000002']
    list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        # list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n' % (wd, year, image_id))
        # list_file.write('C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/JPEGImages/%s.jpg\n' % (image_id))
        convert_annotation(year,image_id)
    list_file.close()
