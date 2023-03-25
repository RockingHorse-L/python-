"""
    打开文件
    对文件操作
    关闭文件
"""
try:
    file = open('123.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    #file.close()这里不会执行
    file.close()
except:
    # # file有值才关闭文件
    # if file:
    # #file.close()这里能关闭
    #     file.close()
    print('出异常了')
    pass
finally:
    if file:
        print('关闭文件')
        # file.close()这里能关闭
        file.close()
    pass
