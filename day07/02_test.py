"""
    JD商城,商城下面有很多店铺（3个），店铺下面有很多商品（3个）
    分析：
        Goods:
            sn
            name
            price
            type
        Shop:
            sn
            name
            goodsList = []

        Mall:
            sn
            name
            type
            shopList = []

"""

class Mall:
    def __init__(self, sn, name):
        self.sn = sn
        self.name = name
        self.type = '生活'
        self.shopList = []

class Shop:
    def __init__(self, sn, name):
        self.sn = sn
        self.name = name
        self.goodsList = []

class Goods:
    def __init__(self, sn, name, price):
        self.sn = sn
        self.name = name
        self.price = price
        self.type = '水'

goods1 = Goods(101, '怡宝', 3)
goods2 = Goods(102, '辣条', 4)
goods2.type = '零食'
goods3 = Goods(103, '纸巾', 5)
goods3.type = '生活用品'

shop1 = Shop(1, '红旗')
shop1.goodsList.append(goods1)
shop2 = Shop(2, '舞东风')
shop2.goodsList.append(goods2)
shop3 = Shop(3, '宜家')
shop3.goodsList.append(goods3)

mall = Mall(1, '万达')
mall.shopList.append(shop1)
mall.shopList.append(shop2)
mall.shopList.append(shop3)

#遍历
for shops in mall.shopList:
    goodsList = shops.goodsList
    for goods in goodsList:
        print(f'商城名：{mall.name}, 商城编号：{mall.sn}, 店铺:{shops.name} 店铺编号: {shops.sn} 商品名称:{goods.name} 商品编号:{goods.sn}')


