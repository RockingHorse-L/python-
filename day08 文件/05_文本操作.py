"""
    文件操作
    1、显示目录
    2、判断文件夹还是文件
    3、对文件进行改名
    4、删除文件
"""

import os

#显示目录
dirs = os.listdir(r'D:\pythonProject3\day08')
print(dirs)

#判断文件夹还是文件
for dir in dirs:
    if os.path.isdir(dir):
        print(f'目录{dir}')
    # if os.path.isfile(dir):
    #     print(f'文件{dir}')

#对文件进行改名
# os.renames(r'D:/pythonProject3/day08 文件/test_b.jpg', r'D:/pythonProject3/day08 文件/test_bbb.jpg')

# 删除文件
os.rmdir('test')

filenpath = r'D:/pythonProject3/day08 文件/test_bak.jpg'
dir, extension = os.path.splitext(filenpath)
print(dir)
print(extension)