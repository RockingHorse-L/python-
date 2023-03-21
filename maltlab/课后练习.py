import random

import matplotlib.pyplot as plt
import numpy as np

students = [
{'name': '张三', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':
80, 'math': 90, 'english': 85},
{'name': '李四', 'gender': 'male', 'age': 16, 'class': 'class2', 'chinese':
70, 'math': 85, 'english': 80},
{'name': '王五', 'gender': 'female', 'age': 15, 'class': 'class3', 'chinese':
90, 'math': 95, 'english': 90},
{'name': '赵六', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':
75, 'math': 80, 'english': 85},
{'name': '钱七', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese':
85, 'math': 90, 'english': 80},
{'name': '孙八', 'gender': 'male', 'age': 19, 'class': 'class2', 'chinese':
90, 'math': 95, 'english': 95},
{'name': '周九', 'gender': 'female', 'age': 18, 'class': 'class3', 'chinese':
80, 'math': 85, 'english': 80},
{'name': '吴十', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese':
70, 'math': 75, 'english': 70},
]

#设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#设置字体大小
plt.rcParams['font.size'] = 10

plt.rcParams['axes.unicode_minus'] = False
# # 饼状图
# femaleCount = 0
# mealCount = 0
# for infoDic in students:
#     for info in infoDic:
#         if infoDic[info] == 'female':
#             femaleCount += 1
#         elif infoDic[info] == 'male':
#             mealCount += 1
#         else:
#             pass
# data = []
# data.append(femaleCount)
# data.append(mealCount)
# label = ['女生', '男生']
# plt.pie(x=data, labels=label)
# plt.show()
#
# #柱状图
# plt.figure(figsize=(20, 8), dpi=100)
# scoreA = 0
# scoreB = 0
# scoreC = 0
# scoreD = 0
# for infoDic in students:
#     for info in infoDic:
#         if info == 'chinese' and infoDic[info] >= 90:
#             scoreA += 1
#         elif info == 'chinese' and infoDic[info] >= 80:
#             scoreB += 1
#         elif info == 'chinese' and infoDic[info] >= 70:
#             scoreC += 1
#         elif info == 'chinese' and infoDic[info] < 70:
#             scoreD += 1
#         else:
#             pass
# score = []
# score.append(scoreA)
# score.append(scoreB)
# score.append(scoreC)
# score.append(scoreD)
# scoreLabel = ['优', '良', '中', '差']
# x = range(len(scoreLabel))
# #绘图 x的轴数, y轴数据, 宽度, 颜色
# plt.bar(x, score, width=0.5, color = ['b', 'r', 'g', 'y'])
#
# plt.xticks(x, scoreLabel)
# plt.show()
#
# #散点图
# chinese = []
# english = []
# for infoDic in students:
#     for info in infoDic:
#         if info == 'chinese':
#             chinese.append(infoDic[info])
#         elif info == 'english':
#             english.append(infoDic[info])
#         else:
#             pass
# # 绘制散点图
# plt.scatter(chinese, english)
# # 显示
# plt.savefig("散点图.jpg")
# plt.show()

#折线图
"""
    分析：
        求不同的年龄他们的数学平均值
        年龄如果已经在age列表里了，那就把相应成绩累加起来存放的字典里
        {18: 265, 16: 85, 15: 95, 17: 155, 19: 95}
        再把各个年龄出现的次数也存放到列表里
        {18: 3, 16: 1, 15: 1, 17: 2, 19: 1}
"""
# sum = 0
# ageDic = {}
# avg = []
# cnt = {}
# count = 0
# for infoDic in students:
#     if infoDic['age'] in ageDic.keys():
#         sum = ageDic[infoDic['age']] + infoDic['math']
#         # print(infoDic['age'])
#         # print(age[infoDic['age']])
#         ageDic[infoDic['age']] = sum
#         count = cnt[infoDic['age']] + 1
#         cnt[infoDic['age']] = count
#     else:
#         ageDic[infoDic['age']] = infoDic['math']
#         cnt[infoDic['age']] = 1
#
# # {18: 265, 16: 85, 15: 95, 17: 155, 19: 95}
# print(ageDic)
# print(cnt)
# #排序，这里保存的是元组的形式
# ageDicSort = sorted(ageDic.items(), key=lambda x: x[0],reverse=False)
# cntDicSort = sorted(cnt.items(), key=lambda x: x[0],reverse=False)
# # print(ageDicSort)
# # 把元组转为字典
# ageDicSort = {k:v for k, v in ageDicSort}
# cntDicSort = {k:v for k, v in cntDicSort}
# print(ageDicSort)
#
# key = []
# value = []
# for avg in ageDicSort:
#     key.append(avg)
#     value.append(ageDicSort[avg] / cntDicSort[avg])
# print(value)
# plt.plot(key, value)
# plt.show()
# 定义字典保存年龄和分数的映射关系
dic = {}
for stuDic in students:
    age = stuDic['age']
    score = stuDic['math']
    # 非首次
    if age in dic:
        # 映射关系 存进去是什么取出来就是什么
        scores = dic[age]
        # print(type(scores))
        scores.append(score)
        pass
    else:
        # 首次
        #dic[18] = [90]
        dic[age] = [score]
# {18: [90, 90, 85], 16: [85], 15: [95], 17: [80, 75], 19: [95]}
# print(dic)
# 求年龄对应的平均分
# avgDic = {} 18: 80多 16:85 15: 95
avgDic = {}
for age, scores in dic.items():
    avgDic[age] = np.mean(scores)
    pass
# {18: 88.33333333333333, 16: 85.0, 15: 95.0, 17: 77.5, 19: 95.0}
# print(avgDic)
print(avgDic.items())
# 参数1 排序的序列当前是字典 key value
# 参数2 当前按照年龄排序
# 参数3 升序降序
# key value
# (18, 88.33333333333333)
# (16, 85.0)
# (15, 95.0)
# (17, 77.5)
# (19, 95.0)
ageGroupScores = sorted(avgDic.items(), key=lambda e:e[0], reverse=False)
# [(15, 95.0), (16, 85.0), (17, 77.5), (18, 88.33333333333333), (19, 95.0)]
# print(ageGroupScores)
#
ages = [ageGroupScore[0] for ageGroupScore in ageGroupScores]
# [15, 16, 17, 18, 19]
print(ages)
scores = [ageGroupScore[1] for ageGroupScore in ageGroupScores]
# [95.0, 85.0, 77.5, 88.33333333333333, 95.0]
print(scores)
plt.plot(ages, scores)
plt.show()