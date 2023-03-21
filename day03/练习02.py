"""
    求解1-100中能被3整除的所有数字的和
"""
sum = 0
for ele in range(0 , 100 , 3):
    sum += ele
print(sum)

"""
    求解1-100中能被3和5同时整除的所有数字的和
"""
sum = 0
for ele in range(0 , 100 ,15):
    sum += ele
print(sum)

"""
    使用while，完成图形的输出
"""
row = int(input('请输入行数：'))
star = 1
while star <= row:
    print('*'*star)
    star += 1



"""
    使用while，完成图形的倒着输出
"""
row = int(input('请输入行数：'))
star = row
while row >= 0:
    print('*'*row)
    row -= 1
