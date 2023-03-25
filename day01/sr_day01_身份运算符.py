"""
    身份运算符用于比较两个值的存储单元是否为同一个
"""
name1 = 'shurui'
name2 = 'shurui'

#name1的内存地址
print(id(name1))

#name2的内存地址
print(id(name2))

#判断是否为同一个内存地址
print(name1 is name2)