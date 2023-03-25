"""
    你和你的女朋友准备出去玩，你的男朋友说出去看电影，女朋友说要学习，怎么办
    剪刀石头布三局两胜，最后显示获胜的一方
    分析
    规则
    rules = (‘剪刀’, '石头', '布')

    区分胜负
    女方获胜
        girlTypeIndex = 0~2
        随机获取女方的出招类型 girlType = rules[girlTypeIndex]

    男方获胜
        boyType
            isGirlSuccess = ((girlType == '剪刀'
"""