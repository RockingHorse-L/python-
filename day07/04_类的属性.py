"""

"""

class GirlFriend:
    #和类绑定的
    count = 0
    def __init__(self, name):
        self.name = name
        #类的属性调用方式， 类名.属性名
        GirlFriend.count += 1
        # self.count = 0
        pass
    # 类方法是和类绑定起来的，正常情况下使用 类名.方法名（[参数列表]）
    # 实例对象也可以调用的原因是，当我们在调用的时候，会将对象所属的类传过去
    @classmethod
    def test(cls):
        print('测试中....')
        pass
    # 静态方法，没有和类及对象绑定，都可访问
    @staticmethod
    def test02(cls):
        print('测试中....')
        pass
    def __del__(self):
        print(f'{self.name}销毁啦')
        pass

girlFriend1 = GirlFriend('婷婷')
# girlFriend1.count += 1
girlFriend2 = GirlFriend('腿腿')
# girlFriend2.count += 1

print(f'女朋友的个数{GirlFriend.count}')

# print(f'女朋友的个数{girlFriend2.count}')
# print(f'女朋友的个数{girlFriend1.count}')
