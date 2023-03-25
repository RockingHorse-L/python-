# letters = 'abcdabcdabcdabcefg'
# words = {}
#
# for num in letters:
#     if num not in words:
#         words[num] = 1
#     else:
#         words[num] += 1
#
# for key , value in words.items():
#     print(key, ':' , value , end='\n')


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

target = int(input('please enter you target num:'))

for num1  in range(1 , len(nums)+1):
    for num2 in range(num1 , len(nums)):
        if num1 + num2 == target:
            print(f"{num1}:{num2}")


