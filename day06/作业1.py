# class Phone:
#     def __init__(self, color, px, price, bound):
#         self.color = color
#         self.px = px
#         self.price = price
#         self.bound = bound
#         pass
#
#     def showInfo(self):
#         print(f'颜色：{self.color}, 屏幕大小：{self.px}, 价格：{self.price}, 品牌：{self.bound}')
#
#
# phone = Phone('深空灰', '1500*1200', 6800, '苹果')
# phone.showInfo()

class Student:
    def __init__(self, name, sex, age, tel, score):
        self.name = name
        self.sex = sex
        self.age = age
        self.__tel = tel
        self.score = score
        pass

    def getScore(self):
        print(f'{self.name}的成绩为{self.score}')

    def getTel(self):
        return self.__tel

    def getStudent(self):
        print(f'姓名：{self.name}, 性别：{self.sex}, 年龄：{self.age}, 电话：{self.__tel}, 成绩：{self.score}')

    def __str__(self):
        return f'姓名：{self.name}, 性别：{self.sex}, 年龄：{self.age}, 电话：{self.__tel}, 成绩：{self.score}'
s1 = Student("学生1", "男", 20, "13600000001", 89)
s2 = Student("学生2", "男", 20, "13600000801", 50)
s3 = Student("学生3", "女", 20, "13600000401", 89)
s4 = Student("学生4", "男", 20, "13600000001", 51)
s5 = Student("学生5", "男", 20, "1520000001", 89)
s6 = Student("学生6", "女", 20, "1520000001", 82)
s7 = Student("学生7", "女", 20, "15200000001", 89)
s8 = Student("学生8", "女", 20, "1892000001", 92)
s9 = Student("学生9", "男", 20, "1820000001", 89)
s10 = Student("学生10", "女", 20, "1520000001", 53)
stus = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

# for i in range(1, 3):
#     stu = Student(input(f'请输入第{i}为学生的姓名'), input(f'请输入第{i}为学生的性别'), input(f'请输入第{i}为学生的年龄'),
#                       input(f'请输入第{i}为学生的电话'), input(f'请输入第{i}为学生的成绩'))
#     stus.append(stu)

# for stude in inputStus(3):
#     print(stude)
#
def failInfo():
    count = 0
    for stu in stus:
        if stu.score < 60:
            stu.getScore()
            count += 1
    return count

print(failInfo())