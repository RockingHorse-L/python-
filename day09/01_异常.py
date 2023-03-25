# file = open('asd.txt' , 'r')
# 0---------
# FileNotFoundError ————》

try:
    #存放可能出现异常的代码
    # num = 1 / 0
    print(num)
    pass
except FileNotFoundError as e:
    print('异常产生了----------', e)
    pass
except ZeroDivisionError as e:
    print('异常产生了----------', e)
    pass
# Exception范围最大
except Exception as e:
    print('异常产生了----------', e)