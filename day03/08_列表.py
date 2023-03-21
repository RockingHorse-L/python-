"""
    列表，容器，添加，删除，修改，查询

"""

# 定义
names = ["shurui" , "tt"]

#添加
names.append('1')
print(names)

#移除
names.remove('1')
print(names)

# 修改
names[0] = 'liangshurui'
print(names)

#查询
print(names[0])

for index, var in enumerate(names):
    print(index , var)
    pass

print('*' * 20)