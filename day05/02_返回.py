"""
    两个数相加
"""

def add(a , b):
    """
    :param a: 被加数
    :param b: 加数
    :return: 返回a+b
    """
    return a + b

def mul(a , b):
    """
    乘法函数
    :param a:
    :param b:
    :return:
    """
    return a * b
#函数的返回值会返回到被调用的地方

def div(a , b):
    """
    除法函数
    :param a:
    :param b:
    :return:
    """
    return a / b
addret = add(5 ,6)
mulret = mul(5 ,6)
divret = div(5 ,6)
print(addret)
print(mulret)
print(divret)

#使用变量进行存储 ab是参数,a+b是表达式,add是变量名
add = lambda a , b : a + b
#调用
ret = add(2 , 3)
print(ret)