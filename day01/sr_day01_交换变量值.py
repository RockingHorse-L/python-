#方法一
a , b = 1, 2
print(a,b)
b , a = 1, 2
print(a,b)

#方法二
a , b = 1, 2
c = 0

c = a
a = b
b = c
print(a,b)

