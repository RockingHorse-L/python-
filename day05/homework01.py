"""
. 定义一个函数,实现返回三个数的和
"""

# def sum(a, b, c):
#     temp = a + b + c
#     return temp
#
# sum_num = sum(1, 2, 3)
# print

# def min_num(a, b, c):
#     minNum = min(a, b, c)
#     return minNum
#
# minNum = min_num(1, 2, 3)
# print(minNum)
#
# def max_num(a, b, c):
#     maxNum = max(a, b, c)
#     return maxNum
#
# maxNum = max_num(1, 2, 3)
# print(maxNum)

# def findIndex(nums, target):
#     #存储目标值和索引
#     idxDic = {}
#     #存储目标值所有索引
#     idxs = []
#     for idx, num in enumerate(nums):
#         if num == target:
#             idxs.append(idx)
#     idxDic[target] = idxs
#     return idxDic
#
# nums = [10, 20, 30, 50, 20]
# ret = findIndex(nums, 20)
# print(ret)
"""
    遍历并用enumerate方法获取元素的值和键值
    当非首次出现的时候，把原有的元素的键值赋值给一个列表，再追加一个当前键值
    首次出现，直接该元素=键值
"""
def indexsOfTarget(nums):
    idxDic = {}
    for idx, num in enumerate(nums):
        #非首次出现
        if num in idxDic:
            #idxs是一个列表
            idxs = idxDic[num]
            idxs.append(idx)
        #首次出现
        else:
            idxDic[num] = [idx]

    return idxDic

nums = [10, 20, 30, 50, 20]
ret = indexsOfTarget(nums)
print(ret)
