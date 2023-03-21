class Prentice:
    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapon = weapon

    def buddha(self):
        print('念佛')

    def doPilgrimage(self):
        print('取经')

    def fight(self):
        print('战斗')

#孙悟空
class WuKong(Prentice):
    def __init__(self, name, age, weapon, characteristic):
        super().__init__(name, age, weapon)
        self.characteristic = characteristic

    def doMaigre(self):
        print('吃斋')

    def extDevi(self):
        print('降妖')

    def buddha(self):
        super().buddha()

    def doPilgrimage(self):
        super().doPilgrimage()

    def fight(self):
        super().fight()

class Pigsy(Prentice):
    def __init__(self, name, age, weapon, characteristic):
        super().__init__(name, age, weapon)
        self.characteristic = characteristic

    def holdHouse(self):
        print('牵马')

    def buddha(self):
        super().buddha()

    def doPilgrimage(self):
        super().doPilgrimage()

    def fight(self):
        super().fight()

class MonkSha(Prentice):
    def __init__(self, name, age, weapon, characteristic):
        super().__init__(name, age, weapon)
        self.characteristic = characteristic

    def pickUpLuge(self):
        print('挑行李')

    def buddha(self):
        super().buddha()

    def doPilgrimage(self):
        super().doPilgrimage()

    def fight(self):
        super().fight()

monkey = WuKong('孙悟空', 1300, '金箍棒', '紧箍咒')
pig = Pigsy('猪八戒', 1250, '九齿钉耙', '嫦娥媳妇')
sha = MonkSha('沙和尚', 1200, '冷兵器', '流沙河')

print(f'{monkey.name}和{pig.name}在{sha.characteristic}，看见了{sha.name}'
      f'在一旁')

sha.doPilgrimage()
