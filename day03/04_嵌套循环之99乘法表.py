"""
    9*9乘法表
"""

## 方式一
# sum = 0
# for num1 in range (1,10):
#     for num2 in range(1,num1 + 1):
#         sum = num1 * num2
#         print(f"{num2} * {num1} = {sum}",end='\t')
#     print('\n')


# 方式二
row = 1 #行
col = 1 #列
while row <= 9:
    while col <= row:
        print(f'{col} * {row} = {col * row}', end='\t')
        col += 1
    row += 1
    col = 1
    print()

