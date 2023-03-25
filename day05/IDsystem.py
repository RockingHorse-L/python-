cards = [
         {'name': 'shurui', 'tel': '1234215123123'},
         {'name': 'tt', 'tel': '5423213154123'}
]

def outInfo():
    """
    :param num: 录入的人数
    :return: 返回的是个人的信息
    """
    num = int(input('please enter num：'))
    # 定义列表存储名片

    cardNums = 0
    # 循环输入名片信息
    while cardNums < num: # 条件
        cardNums += 1
        dic = {} # 输入名片信息存入字典
        name = input('please enter you name: ')
        tel = input('please enter you tel: ')
        dic['name'] = name
        dic['tel'] = tel
        cards.append(dic)
        info = f"""
                {'*' * 50}
                姓名:{name}    电话:{tel}
                {'*' * 50}
        """
        print(info)
        print(cards)




def updataInfo():
    name = input('please enter name of you want to find：')
    #先寻找到这个人的名片
    for cardin in cards:
        if cardin['name'] == name:
            newName = input('Please enter your name with the new one: ')
            newTel = input('Please enter your tel with the new one：')
            cardin['name'] = newName
            cardin['tel'] = newTel
            info = f"""
                        Updated information 
                        {'*' * 50}
                        姓名:{newName}    电话:{newTel}
                        {'*' * 50}
                    """
            print(info)
            print(cards)


#删除信息
def delInfo():
    name = input('please enter name of you want to del：')
    for cardDic in cards:
        if cardDic['name'] == name:
            cardDic.clear()
            break
    print(cards)


outInfo()
updataInfo()
delInfo()
