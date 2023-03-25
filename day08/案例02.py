import json

# 先读取文件
with open('label_train_bak.txt', 'r', encoding='utf-8') as f:
    infoList = f.readlines()
    # print(infoList)
for infos in infoList:
    #json转为python
    infoDic = json.loads(infos)
    dic = infoDic[0]
    print(f'图片：{dic["img"]}, 车牌号：{dic["transcription"]}, 关键点：{dic["points"]}')

