"""
    需求：适用for循环求1~100的奇数和
        for循环9*9乘法表
"""
sum = 0
for ele in range(1 , 100 , 2):
    sum += ele
print(sum)

#9*9乘法表
sum = 0
for num1 in range (1,10):
    for num2 in range(1,num1 + 1):
        sum = num1 * num2
        print(f"{num2} * {num1} = {sum}",end='\t')
    print('')