# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:12:07 2018

@author: Manyue
"""

import cv2
import os
import glob
import numpy as np
import re
import csv
import time


def change_name(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return 2
    elif os.path.isfile(path):
        file_path = os.path.split(path)
        print(file_path[0])
        print(file_path[1])

        file_name = file_path[1]
        file = file_name.split('.')
        print(file[0])
        print(file[1])

        file_type = ['.jpg','.jpeg','png']

        if file[1] in file_type:
            for i in range(len(file)):
                os.rename(path.file_path[0] + '/' + file[0] + i + file[1])
                i=i+1

    elif os.path.isdir(path):
        return 1
    #     for x in os.listdir(path):
    #         name = os.path.join(path.x)
    #         change_name(name)

#img_dir ='C:/Users/Manyue/Desktop/Certis Cisco/NEA/test'
#change_name(img_dir)


def Change_name(path):
    global i

    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        n = len(file_ext)
        if file_ext in img_ext:

            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)

        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            Change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用

img_dir ='C:/Users/Manyue/Desktop/Certis Cisco/NEA/test'
start = time.time()
i = 0
#Change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))









####################################################################################


#with open ('test.csv', 'w', newline = '') as f:
#    thewriter = csv.writer(f)
#    
#    thewriter.writerow(['col1','col2'])
#    thewriter.writerow(['one','two'])

# def get_length(file_path):
#     return 1
#
# def append_data(file_path, name, email):
#     fieldnames = ['id','name','email']
#     next_id = get_length(file_path)
#
#     with open(file_path, "a") as csvfile:
#         writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#         writer.writerow({"id":next_id,"name":name,"email":email})
#
# #append_data("test.csv","Justin","23@jfdsjfdjfo")




def append_data(file_path,category_class, x1, y1, x2, y2):
    global i
    with open (file_path, "a",newline='') as f:
        writer = csv.writer(f)
        img_name = '0000'+ str(i) + '.png'
        writer.writerow([img_name, category_class, x1, y1, x2, y2])
        i+=1

#append_data('NAME.csv','0','232','32424','3432','34')



def rename(path):
    new_path = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/trainset'

    os.rename(img_dir,)

img_dir ='C:/Users/Manyue/Desktop/Certis Cisco/NEA/test'
rename(img_dir)