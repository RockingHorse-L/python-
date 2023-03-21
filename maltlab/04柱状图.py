import matplotlib.pyplot as plt

#设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']
#字体大小
plt.rcParams['font.size'] = 10

# 用于解决绘图时出现负号“-”无法正常显示的问题。具体来说，该代码将参数unicode_minus设置为
# False，表示将使用Unicode字符来显示负号，以解决在某些操作系统或字体下负号显示为方块或其他字符的
# 问题。该设置特别适用于中文环境，因为中文环境中常常使用到特殊字符和符号。
plt.rcParams['axes.unicode_minus'] = False

# 生成画布尺寸：20单位，8单位，dpi为单位分辨率
# figsize是Matplotlib库中figure()函数的一个参数，它控制了图形的大小，以元组形式指定，如
#(20,8)表示图形# 宽度为20英寸，高度为8英寸。如果没有指定，Matplotlib会使用默认值。
# dpi是图形分辨率，即每英寸点数（dots per inch），默认值为100。如果dpi为80
plt.figure(figsize=(20, 8), dpi=80)

#横坐标电影名字
movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记','全球风暴',
'降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
x = range(len(movie_name))
#票房
y = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]

#绘图 x的轴数, y轴数据, 宽度, 颜色
plt.bar(x, y, width=0.5, color = ['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c',
'g', 'g'])
#设置x坐标名字为电影名字
plt.xticks(x, movie_name)
# rotation 文字显示旋转角度
# plt.xticks(x, movie_name, rotation=20)
# 保存图片
plt.savefig(".柱状图1.jpg")
#显示
plt.show()