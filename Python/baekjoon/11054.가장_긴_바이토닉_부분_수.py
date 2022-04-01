import sys
input = sys.stdin.readline
n = int(input())
list = list(map(int, input().rstrip().split()))

dp_left = [1]
dp_right = []
for i in range(1, n):
    left_max = 0
    dp_left.append(1)
    for j in range(i):
        if list[j] < list[i]:
            left_max = max(left_max, dp_left[j])

    dp_left[i] += left_max

for i in range(-1,-n-1,-1):
    right_max = 0
    dp_right.insert(0, 1)
    for j in range(-1, i - 1, -1):
        if list[j] < list[i]:
            right_max = max(right_max, dp_right[j])
    dp_right[i] += right_max

res_max = 0
for i in range(n):
    res_max = max(res_max, dp_left[i] + dp_right[i] - 1)

print(res_max)