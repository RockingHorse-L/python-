"""
    案例：
    GirlFriend有很多爱好，现在她的闺蜜(HoneyFriend)和他的BoyFriend陪她一起学习，或者看电影
    分析
    HoneyFriend
        study(self)
            print('一起学习')
        film(self)
            print('一起看电影')
    boyFriend
        study(self)
            print('一起学习')
        film(self)
            print('一起看电影')
    GirlFriend
        hobbyWithFriend(self, friend)
            friend.study()
            friend.film()
"""
class Friend:
    def __init__(self, name):
        self.name = name

    def study(self):
        print('一起学习')

    def film(self):
        print('一起看电影')

class HoneyFriend(Friend):
    def __init__(self, name):
        # self.name = name
        # super(HoneyFriend, self).__init__()
        super().__init__(name)

    def study(self):
        super().study()
        print(f'{self.name}开心')

    def film(self):
        super().film()
        print(f'{self.name}开心')

class BoyFriend(Friend):
    def __init__(self, name):
        super().__init__(name)

    def study(self):
        super().study()
        print(f'{self.name}很开心')

    def film(self):
        super().film()
        print(f'{self.name}超级开心')

class GirlFriend:
    def __init__(self, name):
        self.name = name

    def hobbyWithFriend(self, friend):
        friend.film()
        friend.study()
        pass

# HyFriend = HoneyFriend('baozi')

ByFriend = BoyFriend('shurui')

girlFriend = GirlFriend('tt')
girlFriend.hobbyWithFriend(ByFriend)
