# import sys
# input = sys.stdin.readline
# N = int(input())
# nums = [int(input()) for _ in range(N)]
# mode_dict = {}
#
# #정렬
# def sort(arr, left, right):
#     mid = left + (right - left)//2 + 1
#     if(right-left < 1):
#         return arr[left:right+1]
#     left_arr = sort(arr, left, mid-1) #left ~ mid
#     right_arr = sort(arr, mid, right) #mid+1 ~ right
#
#     #merge
#     res = []
#     while(True):
#         if(left_arr[0] > right_arr[0]):
#             res.append(right_arr.pop(0))
#         elif(left_arr[0] == right_arr[0]): #let's solve the mode problem here
#             res.append(right_arr.pop(0))
#             res.append(left_arr.pop(0))
#             if(res[-1] not in mode_dict):
#                 mode_dict[res[-1]] = 2
#             else:
#                 mode_dict[res[-1]] += 1
#         else:
#             res.append(left_arr.pop(0))
#
#         if(len(left_arr) == 0):
#             res += right_arr
#             break
#         if(len(right_arr) == 0):
#             res += left_arr
#             break
#     return res
#
# nums = sort(nums, 0, len(nums)-1)
#
# #find mode
# max_keys = sort([k for k, v in mode_dict.items() if max(mode_dict.values()) == v], 0, len(mode_dict)-1)
# if(len(max_keys)==0):
#     mode = nums[1] if N > 1 else nums[0]
# else:
#     mode = max_keys[0] if len(max_keys) == 1 else max_keys[1]
#
# print(round(sum(nums)/N)) #average
# print(nums[N//2])# median
# print(mode)# mode
# print(nums[-1] - nums[0])# range






#------------------------------------------------------------------------------------------------


import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

#find mode
counter = Counter(nums).most_common(2)
if(N > 1):
    mode = counter[0][0] if counter[0][1] > counter[1][1] else counter[1][0]
else:
    mode = nums[0]

print(round(sum(nums)/N)) #average
print(nums[N//2])# median
print(mode)# mode
print(nums[-1] - nums[0])# range




#------------------------------------------------------------------------------------------------