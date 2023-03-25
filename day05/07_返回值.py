"""
    输入数据返回不同的季节
"""

def season(num):
    if num == 1:
        return '春'
    elif num == 2:
        return '夏'
    elif num == 3:
        return '秋'
    elif num == 4:
        return '东'
    else:
        return '未知数据'

ret = season(2)
print(ret)