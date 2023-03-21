"""
分析
    读取里面的数据
    以空格为分隔符存放到列表
    读取出来的内容外面会有一层列表包裹起来
    但是里面的数据是JSON格式，遍历lines 将json转为py

"""
import json

class Car:
    def __init__(self, img, brand, points):
        self.img = img
        self.brand = brand
        self.points = points
def readCarInfo():
    # 打开文件
    file = open('label_train.txt', 'r', encoding='utf-8')
    # 读取文件数据
    lines = file.readlines()
    # print(lines)
    # 保存全部的car数据
    carInfoList = []
    for line in lines:
        # 将json 数据转换为python对象
        # <class 'list'>
        lineInfoList = line.split('\t')
        # print(lineInfoList)
        #第0个是图片地址
        #第1个是jsonstr数据  车的信息 后面的逻辑按照之前的案例即可

        # 存储的汽车的json数据
        carList = json.loads(lineInfoList[1])
        # 将列表中的元素取出来
        carDic = carList[0]
        # print(type(carDic))
        # print(type(carList))
        # print(carList)
        img = lineInfoList[0]
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
