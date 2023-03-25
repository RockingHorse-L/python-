# file = open('data.txt', 'w', encoding='UTF-8')
#追加到后面
file = open('data.txt', 'a+', encoding='UTF-8')
# #写入数据
file.write('第一行')
file.write('第一次\n')
#从文件开始的时候读,0表示将指针移动到起始位置
file.seek(2*3, 0)
# #一行一行的写
# file.writelines(['第二行', '第一次'])
# #关闭
# file.close()

# file = open('data.txt', 'r', encoding='UTF-8')
print(file)

lines = file.read()
print(lines)
for line in lines:
    # line = line.replace('\n', ' ')
    line = line.strip()
