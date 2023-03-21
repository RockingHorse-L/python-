# #打印该目录
# import os
# #相对路径
# #dirs = os.listdir('.')
# #绝对路径
# dirs = os.listdir('D:/pythonProject3/day08 文件')
# print(dirs)
#

# 批量重命名文件
"""
    分析：
        每个名字不一样，但都有序号
        选择1—3的文件进行名字的修改

        先获取文件列表
        通过循环控制次数
"""

import os
#获取目录
dirs = os.listdir('.')
print(dirs)

nums = int(input('请输入想修改的文件个数：'))
for num in range(0, nums):
    # print(dirs[num])
    os.renames(dirs[num],input(f'请输入{dirs[num]}的新名字:'))
