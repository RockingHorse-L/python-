"""
    需求：使用代码给女朋友发1000次我爱你
         打印四次
"""

words = '我爱你'
i = 1
while i <= 1000:
    if i <= 4:
        print(f"第{i}次{words}")
    i = i + 1