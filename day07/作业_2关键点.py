"""
    人有姓名、年龄。根据下面的图形还有很多的关键点landmarks。
    每一个关键点的描述使用 x, y去描 述。
    创建关键点(创建3个即可), 给person人添加关键点之后。遍历每一个关键点

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

class Eye:
    def __init__(self):
        self.type = 'right'
        self.landmarks = []
        pass

class Hand:
    def __init__(self):
        self.type = 'right'
        self.landmarks = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #自定义的类型
        self.eye = Eye()
        self.hand = Hand()

#需求：将眼部的关键，和手部的关键点分别存入眼部关键点和手部关键点

eyePoint1 = Point(100, 200)
eyePoint2 = Point(150, 100)
eyePoint3 = Point(120, 150)

handPoint1 = Point(300, 400)
handPoint2 = Point(400, 500)
handPoint3 = Point(350, 450)

person = Person('tt', 18)
person.eye.type = 'left'
person.eye.landmarks.append(eyePoint1)
person.eye.landmarks.append(eyePoint2)
person.eye.landmarks.append(eyePoint3)

person.hand.landmarks.append(handPoint1)
person.hand.landmarks.append(handPoint2)
person.hand.landmarks.append(handPoint3)

handLandmarks = person.hand.landmarks
eyeLandmarks = person.eye.landmarks
for elm in eyeLandmarks:
    print(f'姓名{person.name}, 年龄{person.age}, 类型{person.eye.type}, 坐标{elm.x},{elm.y}')
for hlm in handLandmarks:
    print(f'姓名{person.name}, 年龄{person.age}, 类型{person.hand.type}, 坐标{hlm.x},{hlm.y}')