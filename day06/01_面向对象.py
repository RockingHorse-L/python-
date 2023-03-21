"""
    女朋友
    特点：黑头发，黄皮肤，性别，年龄
        爱好（hobby）

    类：
    抽象，不具体，是一个模板

    对象：
    年龄：18
    姓名：
    身份证

    特点：
    具体，通过模板创建出来的

    类的声明：
    class 类名：
        成员属性xxx
        成员方法
"""

class GirFriend:
    # 初始化方法
    def __init__(self, name, age=19):
        print('创建')
        self.name = name
        self.age = age
        pass

    #成员方法
    def hobby(self, msg):
        print(f'爱好打球{msg}')
        print(id(self))
        pass
    def showInfo(self):
        print(f'姓名是：{self.name},年龄是:{self.age}')

    def __str__(self):
        return  f'姓名是：{self.name},年龄是:{self.age}'
#找到女朋友，创建对象
#创建对象 变量名 = 类名（参数列表）
#创建对象的时候会调用__init__方法
girlFriend = GirFriend('tt', 20)
print(girlFriend)
#添加属性,对象.属性名
# girlFriend.name = '球球'
# girlFriend.age = 18
#方法的调用
# girlFriend.hobby('超开心')
# girlFriend.showInfo()
# print(f"姓名：{girlFriend.name}, 年龄：{girlFriend.age}")