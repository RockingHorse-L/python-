"""
    1. 随机分配商品
    需求：有三个店铺，6个商品，6个商品随机分配到3个店铺
"""
import random

shopList = [[] , [] , []]
products = ['apple' , 'phone' , 'appleWatch' , 'water' , 'paper' , 'book']

for pro in products:
    num = random.randint(0, 2)
    shopList[num].append(pro)
print(shopList)

"""
    2. 有1，2，3，4四个数字，求这四个数字能生成多少个互不相同且无重复数字的三位数。
"""
flag = 0

for i in range(1 , 5):
    for j in range(1 , 5):
        for k in range(1 ,5):
            if i != j and i != k and j != k:
                flag += 1
print(f"能生成{flag}个互不相同且无重复数字的三位数")
