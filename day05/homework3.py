#方式一
# def info(name, sex, homeAddr):
#     print(f"姓名:{name} 性别:{sex} 家庭地址:{homeAddr}")
#
# name = input('please enter you name:')
# sex = input('please enter you sex:')
# homeAddr = input('please enter you homeAddr:')
# info(name, sex, homeAddr)

# 方式二
def info(**dic):
    print(f"姓名:{dic['name']} 性别:{dic['sex']} 家庭地址:{dic['homeAddr']}")

inName = input('please enter you name:')
inSex = input('please enter you sex:')
inHomeAddr = input('please enter you homeAddr:')
info(name = inName, sex = inSex, homeAddr = inHomeAddr)

# #方式三
# def info(name, **dic):
#     # print(f"姓名:{dic['name']} 性别:{dic['sex']} 家庭地址:{dic['homeAddr']}")
#     return name, dic['sex'], dic['homeAddr']
# dic = {}
# inName = input('please enter you name:')
# inSex = input('please enter you sex:')
# inHomeAddr = input('please enter you homeAddr:')
# dic =
# info(inName, dic)
# print(f"姓名:{dic['name']} 性别:{dic['sex']} 家庭地址:{dic['homeAddr']}")