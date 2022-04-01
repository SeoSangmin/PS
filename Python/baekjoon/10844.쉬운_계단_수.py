import sys
n = int(sys.stdin.readline())
m = 1000000000
dp = [[1 if i==1 else 0 for j in range(10)] for i in range(101)]
dp[1][0] = 0

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = dp[i-1][1] if j==0 else dp[i-1][8] if j == 9 else dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % m)