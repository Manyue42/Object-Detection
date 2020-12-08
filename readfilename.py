import os
import os.path


# # 读取目录下的所有文件，包括嵌套的文件夹
# def GetFileList(dir, fileList):
#     newDir = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/Annotations/'
#     if os.path.isfile(dir):
#         fileList.append(dir)
#     elif os.path.isdir(dir):
#         for s in os.listdir(dir):
#             # 如果需要忽略某些文件夹，使用以下代码
#             # if s == "xxx":
#             # continue
#             newDir = os.path.join(dir, s)
#             GetFileList(newDir, fileList)
#     return fileList


def getFileName(path,fileList):
    if os.path.isfile(path):
        fileList.append(path)
        # print('file')
    elif os.path.isdir(path):
        # print('dir')
        for s in os.listdir(path):
            newDir = os.path.join(path, s)
            getFileName(newDir, fileList)
    return fileList

# path = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/Annotations/'
# folder_path1 = 'C:/Users/Manyue/Desktop/Certis Cisco/NEA-dataset/rawData/NEA_rawData_2'
folder_path1 = 'C:/Users/Manyue/Desktop/train'
folder_path2 = 'C:/Users/Manyue/Desktop/test'
# folder_path = 'C:/Users/Manyue/Desktop/NEA_500/val'
# path = folder_path + '/Annotations/'
path1 = folder_path1 + '/Annotations/'
path2 = folder_path2 + '/Annotations/'
list1 = getFileName(path1,[])
list2 = getFileName(path2,[])

# fo = open("C:/Users/Manyue/Desktop/Certis Cisco/NEA/VOCdevkit/VOC2007/ImageSets/Main/train.txt","w")
fo1 = open(folder_path1 + "/ImageSets/train.txt","w")
fo2 = open(folder_path2 + "/ImageSets/test.txt","w")
for i in list1:
    name = os.path.splitext(os.path.basename(i))[0]
    fo1.write('data/obj/' + name + '.jpg' + '\n')
    print(name)

for n in list2:
    name = os.path.splitext(os.path.basename(n))[0]
    fo2.write('data/obj/' + name + '.jpg' + '\n')
    print(name)

fo1.close()
fo2.close()