"""
    需求：
    1、找出全为255的行数
    2、多少个值是255
    3、去掉所有的255
"""

nums = [
            [255 , 255 , 255 , 255],
            [0 , 255 , 0 , 255],
            [255 , 255 , 255 , 255]
]

count = 0
con = 0
x = 0
for row in nums:
    # print(row)
    for col in row:
        if col == 255:
            count += 1
            x = row.index(col)
            del row[x]
            flag = True
        if flag == True and con <3:
            con += 1
            print(f"第{con}行有255")
            flag = False
            continue
print(f"有{count}个255")
print(nums)

