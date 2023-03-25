"""
    需求：
    1、定义两个变量，分别记录年龄和性别
    2、如果满18岁，并且带有身份证，运行进入网吧上网
"""
age = int(input("年龄："))
sex = input("性别：")
hasCard = True
if age >= 18 and hasCard:
    print("欢迎光临！！！")
else:
    print("出去！！！")