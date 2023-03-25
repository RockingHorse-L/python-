"""
    需求：.输入一个数字将其转换为二进制，判断二进制中1的个数
        比如:
        数字8 转换为二进制 1000 1的个数是1
        数字13 转换为二进制 1101 1的个数是3
"""

number = int(input('please enter you number: '))
flag = 0
sum = number
count = 0
while count <= number/2:
    if sum % 2 == 1:
        flag += 1
    sum = int(sum / 2)
    count += 1
print(f"1的个数是{flag}")
