"""
    商城下面有店铺，店铺下面有商品
"""
import json
# dic = {
#     "name":"JDmall",
#     "sn" : 10,
#         "shops":[
#             {
#                 "name":"XiaoMi",
#                 "goods":"XiaoMi9"
#             },
#             {
#                 "name":"HuaWei",
#                 "goods":"note11"
#             },
#             {
#                 "name":"apple",
#                 "goods":"iphone14pro max"
#             }
#         ]
# }
dic = {
     "name":"shurui",
     "age" : 18,
}
jsonStr = json.dumps(dic)
print(jsonStr)

# file = open('user.txt', 'w', encoding='utf-8')
# file.write(jsonStr)
# file.close()

# file = open('user.txt', 'r', encoding='utf-8')
# users = file.readlines()
#
# for user in users:
#     # 方式1 使用字符串的方式截取或者分割
#     print(user)
#     #将json转换为字典
#     userDic = json.loads(user)
#     print(userDic['name'])
#     print(userDic['age'])