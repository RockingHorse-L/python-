import math

import numpy as np


def getAngle(sta_point, mid_point, end_point):
    ma_x = sta_point[0] - mid_point[0]
    ma_y = sta_point[1] - mid_point[1]
    mb_x = end_point[0] - mid_point[0]
    mb_y = end_point[1] - mid_point[1]
    ab_x = sta_point[0] - end_point[0]
    ab_y = sta_point[1] - end_point[1]
    ab_val2 = ab_x * ab_x + ab_y * ab_y
    ma_val2 = ma_x * ma_x + ma_y * ma_y
    mb_val2 = mb_x * mb_x + mb_y * mb_y
    cos_M = (ma_val2 + mb_val2 - ab_val2) / (2 * np.sqrt(ma_val2) * np.sqrt(mb_val2))
    angleAMB = np.arccos(cos_M) / np.pi * 180
    return angleAMB

def get_angle_v2(a, b, c):
    '''
    计算角度
    :param a:
    :param b:
    :param c:
    :return:
    '''

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def getDistance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def angle_test():
    a = np.array([0, 30, 45, 60, 90])
    print('不同角度的正弦值：')
    # 通过乘 pi/180 转化为弧度
    print(np.sin(a * np.pi / 180))
    print('数组中角度的余弦值：')
    print(np.cos(a * np.pi / 180))
    print('数组中角度的正切值：')
    print(np.tan(a * np.pi / 180))


if __name__ == '__main__':
    a = (5, 1)
    b = (1, 1)
    # c = (2, 5)
    c = (1, 5)

    # abx = a[0] - b[0]
    # aby = a[1] - b[1]
    # print(abx**2)
    # print(aby**2)
    # cbx = c[0] - b[0]
    # cby = c[1] - b[1]
    # print(cbx**2)
    # print(cby**2)

    # print(getAngle(a, b, c))
    # print(get_angle_v2(b, a, c))




