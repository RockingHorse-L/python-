"""
    案例：GirlFriend很喜欢学习，大学期间学习了很多课程,Linux, AI, DataBase
    每学一门课程，打印相应的内容

    要实现多态：
        要有继承
"""
class Course:
    def showInfo(self):
        print('正在学习')

class Linux(Course):
    def showInfo(self):
        print('正在学linux')
    pass
class AI(Course):
    def showInfo(self):
        print('正在学AI')
    pass
class DataBase(Course):
    def showInfo(self):
        print('正在学DataBase')
    pass
class GirlFriend:

    def __init__(self, name):
        self.name = name

    def study(self, course):
        course.showInfo()
        pass

linux = Linux()
ai = AI()
dataBase = DataBase()

girlFriend = GirlFriend('tt').study(linux)