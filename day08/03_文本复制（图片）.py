"""
    准备源文件，目标文件
    从源文件 读取文本数据 到内存  写入目标文件
    关闭源文件 目标文件

    使用with语句处理文件的时候，他会自动关闭文件
"""

with open('test.jpg', 'rb') as srcFile:
    lines = srcFile.readlines()
with open('test_b.jpg', 'wb') as targetFile:
    targetFile.writelines(lines)