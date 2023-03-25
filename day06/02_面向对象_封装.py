"""
    封装：
        保证数据的一个安全性
        讲细节封装起来，防止外部能够随意的改动
"""

class GirFriend:
    # 初始化方法
    def __init__(self, name, age=19):
        print('创建')
        self.name = name
        #私有化，在属性前面加两个下划线，外面就不能够随意访问了，怎么办
        #提供一种供外部访问的功能
        if age < 0:
            age = 16
        self.__age = age
        pass
    #供外部访问
    def getAge(self):
        return self.__age

    #成员方法
    def hobby(self, msg):
        print(f'爱好打球{msg}')
        pass
    def showInfo(self):
        print(f'姓名是：{self.name},年龄是:{self.age}')

    def __str__(self):
        return  f'姓名是：{self.name},年龄是:{self.age}'

#创建对象
# girFriend = GirFriend('tt', 18)
girFriend = GirFriend('tt', -18)
#语法没错为u，但是不符合逻辑，年龄不能为负数，怎办？私有化，在属性前面加两个_
# girFriend.showInfo()
print(f"姓名：{girFriend.name}, 年龄：{girFriend.getAge()}")
