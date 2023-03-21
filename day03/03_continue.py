"""
    需求：使用代码给女朋友发1000次我爱你
         跳过第44次
"""


words = '我爱你'
i = 1
while i <= 100:
    if i ==44:
        i += 1
        #结束当前这一次循环
        continue
    print(f"第{i}次{words}")
    i += 1