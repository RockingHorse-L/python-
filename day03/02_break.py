"""
    需求：使用代码给女朋友发1000次我爱你
         第60次的时候结束
"""


words = '我爱你'
i = 1
while i <= 1000:
    print(f"第{i}次{words}")
    if i ==60:
        break
    i = i + 1