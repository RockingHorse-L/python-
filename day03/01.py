"""
    列表生成式构造：【元素 迭代表达式 条件表达式】

"""

# nums = [var for var in range(1 , 11)]
# print(nums)

# nums = [var for var in range(1 , 101) if var % 2 == 0]
# print(nums)

import random
shopList = [[] , [] , []]
products = ['apple' , 'phone' , 'appleWatch' , 'water' , 'paper' , 'book']
for pro in products:
    num = random.randint(0, 2)
    shopList[num].append(pro)
print(shopList)
