"""
    nums1 = [1, 2, 1, 4, 5, 1, 2, 1, 4, 5, 1, 2, 1, 4, 5]
    nums2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    请问nums2中的元素在nums1中出现的次数
    打印形式:
    1: 6
    2: 3

"""
nums1 = [1, 2, 1, 4, 5, 1, 2, 1, 4, 5, 1, 2, 1, 4, 5]
nums2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

list = []
dic = {}
#先取出nums2的值
for numdic in nums2:
    # print(numdic)
    #先把nums2中值存放在dic，可避免重复
    if numdic not in list:
        list.append(numdic)
# print(dic)

for num in list:
    dic[num] = nums1.count(num)
print(dic)
# for num in list:
#     #拿num里的值与nums1作比较
#     for num1 in nums1:
#         if num == num1 or num not in nums1:
#             dic[num] =
#     #首次出现
#         else:
#             dic[num] = 1
# print(dic)
