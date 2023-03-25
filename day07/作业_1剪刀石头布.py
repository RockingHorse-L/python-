"""
    你和你的女朋友今天准备出去玩：你的男朋友说要出去看电影，女朋友说要学习。
    怎么办? 剪刀石头布游戏 3局两胜。请最后显示 获胜的是哪一方?
"""

import random

class Friend:
    def __init__(self, name):
        self.name = name
        self.score = 0
        pass

class Game:

    #游戏数据初始化
    def __init__(self, girlFriend, boyFriend):
        self.girlFriend = girlFriend
        self.boyFriend = boyFriend
        self.rules = ('剪刀', '石头', '布')

    def playing(self, cnt=3):
        rules = self.rules
        equalScore = 0
        #获取女朋友出招情况
        for num in range(cnt):
            girlTypeIndex = random.randint(0, 2)
            girlType = rules[girlTypeIndex]
            boyTypeIndex = random.randint(0, 2)
            boyType = rules[boyTypeIndex]

            if (girlType == '剪刀' and boyType == '布') \
                    or (girlType == '石头' and boyType == '剪刀') \
                    or (girlType == '布' and boyType == '石头'):
                self.girlFriend.score += 1
            elif girlType == boyType:
                equalScore += 1
                pass
            else:
                self.boyFriend.score += 1
                pass
        return self.girlFriend.score, self.boyFriend.score, equalScore
girlFriend = Friend('tt')
boyFriend = Friend('shurui')
game = Game(girlFriend, boyFriend)
scoreTuple = game.playing()
# print(scoreTuple)
print(f'女方:{scoreTuple[0]} 男方:{scoreTuple[1]} 平局:{scoreTuple[2]}')
# 存在平局大于0的情况
while scoreTuple[2] > 0:
    scoreTuple = game.playing(scoreTuple[2])
    print(f'女方:{scoreTuple[0]} 男方:{scoreTuple[1]} 平局:{scoreTuple[2]}')
print('---------------')
print(f'女方:{scoreTuple[0]} 男方:{scoreTuple[1]} 平局:{scoreTuple[2]}')