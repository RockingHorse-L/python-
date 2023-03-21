"""
    需求：
    1、找出全为255的行数
    2、多少个值是255
    3、去掉所有的255

    分析：
        取出数据，但外面套了一层
        列表中每个数都为255则满足1
"""

nums = [
            [255 , 255 , 255 , 255],
            [0 , 255 , 0 , 255],
            [255 , 255 , 255 , 255]
]


count = 0
row = 0
list = []
for numlist in nums:
    # print(numlist)
    for num in range(len(numlist)):
        if numlist[num] == 255:
            count += 1
            flag = True
    if flag == True :
        list.append(row)
print(list)





# for row in nums:
#     # print(row)
#     for col in row:
#         if col == 255:
#             count += 1
#             x = row.index(col)
#             del row[x]
#             flag = True
#         if flag == True and con <3:
#             con += 1
#
#             flag = False
#             continue
# print(f"有{count}个255")
# print(nums)

