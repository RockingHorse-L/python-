# def num99(num):
#     for num1 in range (1,num + 1):
#         for num2 in range(1,num1 + 1):
#             sum = num1 * num2
#             print(f"{num2} * {num1} = {sum}",end='\t')
#         print('\n')
#
# num = int(input('please enter you number:'))
# num99(num)


# def factorial(num):
#     sum = 1
#     for i in range(1, num + 1):
#         sum *= i
#     return sum
#
# num = int(input('please enter you num: '))
# print(factorial(num))

def factorial(num):
    sum_end = 0
    for i in range(1, num + 1):
        sum = 1
        for j in range(1, i + 1):
            sum *= j
        sum_end += sum
    return sum_end

num = int(input('please enter you num: '))
print(factorial(num))