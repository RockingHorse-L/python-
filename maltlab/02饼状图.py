import  matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
data = [0.2515, 0.3724, 0.2312, 0.02323, 0.3322]
labels = ['美国', '中国', '英国', '法国', '荷兰']
plt.pie(x=data, labels=labels)
plt.show()