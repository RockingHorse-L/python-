"""
    自定义需求:完成类似上课讲的人有眼睛眼睛有类型眼睛有关键点这种需求
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#眼部关键点和类型
class LeftEye:
    def __init__(self):
        self.type = 'left'
        self.leftEye = []

class RightEye:
    def __init__(self):
        self.type = 'right'
        self.rightEye = []


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.leye = LeftEye()
        self.reye = RightEye()

eyePoint1 = Point(100, 200)
eyePoint2 = Point(150, 100)
eyePoint3 = Point(120, 150)

person = Person('tt', 18)

person.leye.leftEye.append(eyePoint1)
person.leye.leftEye.append(eyePoint2)
person.reye.rightEye.append(eyePoint3)

LeftEye = person.leye.leftEye
rightEye = person.reye.rightEye
for le in LeftEye:
    print(f'姓名{person.name}, 年龄{person.age}, 类型{person.leye.type }, 坐标{le.x},{le.y}')

for re in rightEye:
    print(f'姓名{person.name}, 年龄{person.age}, 类型{person.reye.type}, 坐标{le.x},{le.y}')