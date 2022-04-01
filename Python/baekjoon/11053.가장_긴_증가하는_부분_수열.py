# import sys
# n = int(sys.stdin.readline())
# list = list(map(int, sys.stdin.readline().rstrip().split()))
# dp = [1]
# for i in range(1, n):
#     max_value = 0
#     dp.append(1)
#     for j in range(i):
#         if list[j] < list[i]:
#             max_value = max(max_value, dp[j])
#     dp[i] += max_value
#
# print(max(dp))




##others
import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for arr_i in arr:
    if arr_i > dp[-1]:
        dp.append(arr_i)
    else:
        idx = bisect.bisect_left(dp, arr_i)
        dp[idx] = arr_i

print(len(dp))