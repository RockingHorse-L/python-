"""
    需求
    有个小孩，喜欢编程，找家教，要求：家教老师会编程

    老师：
        Student
            name
            行为：program
                print('学生教编程')
        Robot:
            name
            行为：program
                print('机器人教编程')
        Teacher
            name
            行为：program
                print('老师教编程')
        Child:
            study(self, tutor)
            tutor.program()
"""
class Tutor:
    def program(self):
        print('教编程')

class Student(Tutor):

    # def __init__(self, name):
    #     self.name = name

    def program(self):
        print(f'学生{self.name}教编程')

class Teacher(Tutor):

    # def __init__(self, name):
    #     self.name = name

    def program(self):
        print(f'老师{self.name}教编程')

class Robot(Tutor):

    # def __init__(self, name):
    #     self.name = name

    def program(self):
        print(f'机器人{self.name}教编程')
#闭合
class Child:
    def __init__(self, name):
        self.name = name

    def study(self, tutor):
        tutor.program()
        pass

child = Child('tt')
teacher = Teacher('shurui')
child.study(teacher)