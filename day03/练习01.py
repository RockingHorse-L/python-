"""
    需求：计算面馆销售额
        通过键盘输入：每天卖出多少碗面
        通过键盘输入：每碗面条多少钱
        通过键盘输入：今年共营业多杀天
        计算并输出一年的总销售额
"""

count = input('每天卖出多少碗面:')
money = input('每碗面条多少钱：')
days = input('今年共营业多少天：')

sales = int(count) * float(money) * int(days)

print("今年共营业"+str(sales)+"元")

