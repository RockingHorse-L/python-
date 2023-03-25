"""
    案例2：定义一个狗类，继承自动物类，定义一个猫类，继承自动物类，动物类有方法makeSound
    Dog类和Cat类分别继承Animal类，并覆写父类方法makeSound

    作用：
        简化代码
"""

class Animal:
    def __init__(self, name):
        self.name = name
        pass

    def makeSound(self):
        print('叫~~')
        pass
"""
    因为Dog和cat有共同的属性和方法，抽取到Animal类里面 怎么关联？继承
    
    class 子类（父类）
        ....
"""
class Dog(Animal):

    def __init__(self, name):
        # self.name = name
        super().__init__(name)
        pass
    #将父类的方法进行覆写
    def makeSound(self):
        super().makeSound()
        print(f'{self.name}wang~~')
        pass


class Cat(Animal):

    def __init__(self, name):
        # self.name = name
        #调用父类的方法
        super().__init__(name)
        pass
# 重写父类的方法：方法名和参数保持一致--》直接把父类的方法拷贝在了子类即可，然后拓展
    def makeSound(self):
        super().makeSound()
        print(f'{self.name}miao~~')
        pass

dog = Dog('旺财')
dog.makeSound()
cat = Cat('喵喵')
cat.makeSound()