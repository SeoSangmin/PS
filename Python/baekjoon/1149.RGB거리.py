import sys
dp = []
n = int(sys.stdin.readline())

rgb = [[int(i) for i in sys.stdin.readline().split()] for _ in range(n)]

for idx in range(1, n):
    rgb_now = rgb[idx]
    rgb_now[0] = rgb_now[0] + min(rgb[idx-1][1], rgb[idx-1][2])
    rgb_now[1] = rgb_now[1] + min(rgb[idx - 1][0], rgb[idx - 1][2])
    rgb_now[2] = rgb_now[2] + min(rgb[idx - 1][0], rgb[idx - 1][1])

print(min(rgb[n-1]))
