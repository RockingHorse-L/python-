"""
    需求：
    1、输入一个成绩。
    2、成绩等级为（A,B,C,D,E）
    成绩大于90为A
    成绩大于80为B
    成绩大于70为C
    成绩大于60为D
    成绩低于60为E


"""

score = int(input("请输入成绩："))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")