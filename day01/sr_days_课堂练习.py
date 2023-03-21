"""
    1~100的和
    1~100的奇数和
    打印出1-100的值
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i = i + 1
print(f"1~100的和：{sum}")

i = 1
sum = 0
while i <= 100:
    if i % 2 == 1:
        sum += i
        i = i + 1
    else:
        i += 1
print(f"奇数和：{sum}")

i = 1
while i <= 100:
    print(i)
    i += 1



