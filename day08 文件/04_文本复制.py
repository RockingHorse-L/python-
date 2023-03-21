"""
    准备源文件，目标文件
    从源文件 读取文本数据 到内存  写入目标文件
    关闭源文件 目标文件
"""
srcFile = open('data.txt', 'r', encoding='UTF-8')
#读取文件数据存放到列表中
lines = srcFile.readlines()
targetFile = open('data_bak.txt', 'a', encoding='UTF-8')
targetFile.writelines(lines)
