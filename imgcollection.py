# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:31:48 2018

@author: Manyue
"""

import urllib.request
import cv2
import numpy as np
import os
import glob


#image = cv2.imread("C:/Users/Manyue/Desktop/Certis Cisco/mug_test/pos/1.jpg",cv2.IMREAD_GRAYSCALE)
#cv2.imshow("original", image) 
#cv2.waitKey(0)
#resized_image = cv2.resize(image,(50,50))
#cv2.imwrite("C:/Users/Manyue/Desktop/Certis Cisco/mug_test/pos/1.jpg", resized_image)


# image = cv2.imread("C:/Users/Manyue/Desktop/Certis Cisco/pos/1.jpg",cv2.IMREAD_GRAYSCALE)
# resized_image = cv2.resize(image,(50,50))
# cv2.imwrite("C:/Users/Manyue/Desktop/Certis Cisco/pos/1.jpg", resized_image)



def store_raw_images():
    # neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03365592'
    # neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n09282208'
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n03758089'

    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 3302
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/img_"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))      
# store_raw_images()

def find_uglies():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('This is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
# find_uglies()
                    

def create_pos_n_neg():
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n' # fix size of the positive image
                with open('info.dat', 'a') as f:
                    f.write(line)

                
                
#store_raw_images()
#find_uglies()
# create_pos_n_neg()


# i = 3260
# dir = 'C:/Users/Manyue/Desktop/neg'
# dir = os.path.join(dir,'*')
# dir = glob.glob(dir)
# for img in dir:
#     name = os.path.basename(img)
#     img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
#     resized = cv2.resize(img, (100,100))
#     cv2.imwrite('C:/Users/Manyue/Desktop/store/' + 'neg_' + str(i) + '.jpg',resized)
#     i+=1