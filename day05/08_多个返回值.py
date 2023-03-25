"""
    同时对x,y进行求和，加减运算
"""

def add_subtract(x, y):
    add = x + y
    sub = x - y
    return add , sub

ret = add_subtract(5, 1)
print(ret)