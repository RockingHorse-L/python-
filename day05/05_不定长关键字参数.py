"""
    打印包含姓名，年龄等学生信息的函数
"""
#针对学生信息不知道有多少个可以使用
def printInfo(name, age, **dic):
    print(f"学生信息：{name} 年龄：{age} 职业:{dic['job']} 身高：{dic['height']} 体重：{dic['weight']}")
    pass

dic = {'job':'actor',
       'height':170,
       'weight':100}

printInfo('赵磊', 26, job='卖py', height=160, weight=210)