
# 定义数据
dataInfo = [
            ['path', 'x', 'y', 'w', 'h'],
            ['1.png', '100', '100', '200', '200'],
            ['2.png', '50',  '100', '100', '100'],
            ['3.png', '200', '50',  '150', '100'],
            ['4.png', '150', '100', '100', '100']
  ]

file = open('shurui.txt', 'w+', encoding='UTF-8')
# 将数据写入文件
for datas in dataInfo:
    for data in datas:
        # print(data)
        file.write(f'{data}\t')
    file.write(f'\n')
file.close()

# 读取文件并存入到dataDic
dataDic = {}
# 读取文件
with open('shurui.txt', 'r', encoding='UTF-8') as f:
    f.seek(15)
    dataLines = f.readlines()
    for datas in dataLines:
        #可以取出相应位置元素作为key
        # print(datas[:5])
        key = datas[:5]
        # print(key)
        value = datas[6:]
        # value = value.strip().split('\t')
        value = value.split()
        # print(value)
        dataDic[key] = value
print(dataDic)