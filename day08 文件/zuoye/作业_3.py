"""
    文件路径
"""

import os
def GetPath(path, isTrain=True):
    datalist = []
    dic = {}
   # 判断是训练集还是测试集
    if isTrain:
        # 加路径
        datasetPath = path + '\\' + 'TRAIN'
    else:
        datasetPath = path + '\\' + 'TEST'

    labels = os.listdir(datasetPath)
    # print(labels)
    # 遍历labels下面的图片
    for label in labels:
        labelPath = datasetPath + '\\' +label
        # print(label)
        files = os.listdir(labelPath)
        #存储标签下面对应的文件路径
        for file in files:
            filepath = labelPath + '\\' + file
            datalist.append(file)
            dic[label] = datalist
    return dic

path = r"C:\Users\Administrator\PycharmProjects\pythonProject1\day08\zuoye\MNIST"

print(GetPath(path, True))
