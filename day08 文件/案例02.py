"""
分析
    读取里面的数据
    读取出来的内容外面会有一层列表包裹起来
    但是里面的数据是JSON格式，遍历lines 将json转为py

"""
import json

#方式一
# import json
#
# # 先读取文件
# with open('label_train_bak.txt', 'r', encoding='utf-8') as f:
#     infoList = f.readlines()
#     # print(infoList)
# for infos in infoList:
#     #json转为python
#     infoDic = json.loads(infos)
#     dic = infoDic[0]
#     print(f'图片：{dic["img"]}, 车牌号：{dic["transcription"]}, 关键点：{dic["points"]}')


# #方式二
class Car:
    def __init__(self, img, brand, points):
        self.img = img
        self.brand = brand
        self.points = points
def readCarInfo():
    # 打开文件
    file = open('label_train_bak.txt', 'r', encoding='utf-8')
    # 读取文件数据
    lines = file.readlines()
    # print(lines)
    # 保存全部的car数据
    carInfoList = []
    for line in lines:
        # 将json 数据转换为python对象
        # <class 'list'>
        # 存储的汽车的json数据
        carList = json.loads(line)
        # 将列表中的元素取出来
        carDic = carList[0]
        # print(type(carDic))
        # print(type(carList))
        print(carList)
        img = carDic['img']
        brand = carDic['transcription']
        points = carDic['points']
        # print(f'图片地址:{img} 车牌号:{brand} 坐标:{points}')
        # 创建对象存储数据
        car = Car(img, brand, points)
        # 添加每一辆car
        carInfoList.append(car)
        # 返回
        #print(type(carInfoList))
    return carInfoList
# readCarInfo()
carList = readCarInfo()
#遍历carList
# print(carList)
for carObj in carList:
    print(f'图片地址:{carObj.img} 车牌号:{carObj.brand} 坐标:{carObj.points}')

# """
#     一步一步走
#
#     再把取出来的信息放到Car的对象中 所以我们要新建一个类
# """
# class Car:
#     def __int__(self, img, brand, points):
#         self.img = img
#         self.brand = brand
#         self.points = points
#         pass
#
# def readCarInfo():
#     #打开文件
#     file = open('label_train_bak.txt', 'r', encoding='utf-8')
#     #读取文件数据
#     lines = file.readlines()
#     #打印出来可以知道要处理一些符号。比如换行符
#     # print(lines)
#     #保存全部car的数据
#     carInfoList = []
#     for line in lines:
#         # 将数据转为py
#         carList = json.loads(line)
#         # 将列表元素取出来为字典
#         carDic = carList[0]
#         # print(type(carDic))
#         # print(type(carList))
#         # print(carList)
#         img = carDic['img']
#         brand = carDic['transcription']
#         points = carDic['points']
#         print(f'图片地址：{img}')
#         car = Car(img, brand, points)
#         carInfoList.append(car)
#
#     return carInfoList
#
#
# carList = readCarInfo()
# print(carList)