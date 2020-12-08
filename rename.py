import os
import os.path
import csv


# This script can rename & change image type
# Can only proceed image files under the folder, cannot proceed into sub-directory
def renameImg(basepath,startNum):
    img_types = ['..jpg', '..jpeg', '..png']
    imgs = []
    dir = []
    for dirpath, dirnames, fnames in os.walk(basepath):
        imgs.extend(fnames)
        print (imgs)

    for filename in imgs:
        newname = "00000%d.jpg" %startNum
        os.rename(basepath+filename, basepath+newname)
        with open(file_path, "a") as f:
            f.writelines("00000" + str(startNum) + '\n')
        startNum+=1

if __name__=='__main__':
    # basepath = str(input("Enter the folder's path (end with /):"))
    # basepath = '/Users/Manyue/Desktop/Certis Cisco/NEA/test/traindata/'
    basepath = '/Users/Manyue/Desktop/Certis Cisco/data/NEA_rawData_10/JPEGImage/'
    file_path = '/Users/Manyue/Desktop/Certis Cisco/data/NEA_rawData_10/ImageSets/train.txt'
    print("Your image's folder path is: %s" %(basepath))
    startNum = int(input("Enter the start counting number :"))
    renameImg(basepath,startNum)
