"""
    2. 写代码，有如下变量，请按照要求实现每个功能 name = " posekakaka "
        a. 移除name 变量对应的值两边的空格，并输出移除后的内容 name = "posekakaka"
        b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
        c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
        d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
        e. 将name 变量对应的值根据 “k” 分割，并输出结果。
        f. 请问，上一题 e 分割之后得到值是什么类型（可选）
    3. 列表students中保存了6个学生的信息 students = [
        {'name':'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel':'15300022839'},
        {'name':'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel':'15300022838'},
        {'name':'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel':'15300022837'},
        {'name':'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel':'15300022428'},
        {'name':'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel':'15300022653'},
        {'name':'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel':'15300022867'}
]
        3.1 遍历所有的姓名
        3.2 统计不及格学生的个数
        3.3 打印所有男生的信息
        3.4 求平均分数
"""
# name = " posekakaka "
# name.split()
# print(name)
# newName = 'posekakaka'
# print(newName.startswith('po'))
# print(newName.endswith('a'))
# print(newName.replace('k' , 'c'))
#
# print(newName.split('k'))
# print(type(newName.split('e')))

students = [
        {'name':'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel':'15300022839'},
        {'name':'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel':'15300022838'},
        {'name':'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel':'15300022837'},
        {'name':'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel':'15300022428'},
        {'name':'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel':'15300022653'},
        {'name':'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel':'15300022867'}
]

# for person in students:
#     for key in person.keys():
#         if key == 'name':
#             print(person[key])

# count = 0
# for person in students:
#     for key in person.keys():
#         if key == 'score':
#             if person[key] < 60:
#                 count += 1
# print(f"不及格的有{count}人")

# for person in students:
#     for key in person.keys():
#         if key == 'sex':
#             if person[key] == '男':
#                 print(person)

sum = 0
count = 0
for person in students:
    for key in person.keys():
        if key == 'score':
            sum += int(person[key])
            count += 1
print(f"评价分数为{sum/count}")