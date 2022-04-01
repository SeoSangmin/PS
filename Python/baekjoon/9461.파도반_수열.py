import sys
t = int(sys.stdin.readline())

dp = [0 for _ in range(101)]
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for _ in range(t):
    x = int(sys.stdin.readline())
    if x < 6:
        print(dp[x])
        continue
    for i in range(5, x+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[x])