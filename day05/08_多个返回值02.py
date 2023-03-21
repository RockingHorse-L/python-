"""
    求a, b, c的最小值 最大值
"""

def extremun(a, b, c):
    min_num = min(a, b, c)
    max_num = max(a, b, c)
    return min_num, max_num

ret = extremun(10, 2, 31)
print(ret)