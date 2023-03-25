"""
    定义一个方法，传入两个参数，一个表示活泼的价格，一个类型的折扣，返回货品总价格（使用可变参数）
    分析：
    折扣          cutoff
    多个货品的价格  tuple->goodPrices(1.1, 2.1, 3.0)
"""

# def salePrice(cutoff , goodsPrices):
#     total = 0
#     for price in goodsPrices:
#         total += price
#     return total * cutoff
#
# goodsPrices = (1.1, 2.1, 3.0)
# ret = salePrice(0.5, goodsPrices)
#
# print(ret)

"""
    不定长参数
    def 函数名([其他形式参数] , *可变形式参数）
"""
#针对不知道有多少个数据时使用
def salePrice(cutoff , *goodsPrices):
    #元组
    total = 0
    for price in goodsPrices:
        total += price
    return total * cutoff

ret = salePrice(0.5, 1.0, 2.0, 3.0, 4.0, 5.0)

print(ret)