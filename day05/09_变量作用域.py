y = '全局'

def fn():
    #把y值弄成全局变量
    global y
    y = '局部'
    print(y)

fn()
print(y)