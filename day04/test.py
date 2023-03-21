# name = 'shurui ai tingting'
# filepath = 'c:/python/AI/15/str'
# print(filepath.rsplit('/', 4))
# #按照/来分割，4为分割的次数
#
# print(name.split(' ' , 2))
# print(name.splitlines())
# print(name.split())
# print(name.split(','))
""" 字典: {key : value} 常用操作: 增加 删除 修改
"""
dic = {'name': '球球', 'age': 19, 'sex': '女'}
print(dic)

# 添加
dic['addr'] = '四川'
print(dic)

# # 删除
# del dic['addr']
# print(dic)
# dic.pop('sex')
# print(dic)
#
# # 修改
# dic['age'] = 20
# print(dic)
#
# # 查询
# print(dic['age'])
#
# 获取字典的键值
print(dic.keys())
for key in dic.keys():
    print(f'{key}:{dic[key]}', end=' ')

# 获取字典中的所有值
print(dic.values())
for value in dic.values():
    print(value, end=' ')
print() # 遍历键值对
print('遍历键值对')

for key, value in dic.items():
    print(key, ":", value, end=' ')
# 判断键值是否在字典中存在 print('name' in dic) # 清空字典
dic.clear()