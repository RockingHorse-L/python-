"""
    名片管理 系统 录入三张名片即可 名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
    cards = [
    {“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
     {名片信息2},
     {名片信息3}
    ]
    需要完成的功能 就是对 名片盒子 进行增删改查
        1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字 典)
        2. 显示所有名片: 遍历名片盒子输出名片信息
        3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片, 如果找到 , 重写录入新的名片信息, 完成修改操作
        4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
cards = [
    {"name":"张三", "tel":"13812345678", "job":"CEO", "addr":"四川"},  # 字典
    {"name":"李四", "tel":"13823123133", "job":"CTO", "addr":"四川"},
    {"name":"shurui", "tel":"15692348791", "job":"老总", "addr":"四川"}
]
# inName = input('请输入用户名：')
# inTel = input('请输入电话号码:')
# inJob = input('请输入工作职位：')
# inAddr = input('请输入工作地址：')
#
# inCards = {}
# inCards["name"] = inName
# inCards["tel"] = inTel
# inCards["job"] = inJob
# inCards["addr"] = inAddr
# cards.append(inCards)
#
# i = 0
#
# for person in cards:
#     for key , value in person.items():
#         print(key , ':' , value , end=' ')

#输入姓名，遍历查找，再判断是否查找到，修改更新
# selectName = input('请输入查找的姓名：')
#
# for person in cards:
#     for key in person.keys():
#         if key == 'name':
#             if person[key] == selectName:
#                 newName = input('请输入新的名字：')
#                 person[key] = newName
#                 person["name"] = person[key]
#                 break
# print(cards)

selectName = input('请输入查找的姓名：')

for person in cards:
    for key in person.keys():
        if key == 'name':
            if person[key] == selectName:
                person.clear()
                break
print(cards)