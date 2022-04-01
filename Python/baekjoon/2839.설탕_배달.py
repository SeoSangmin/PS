import sys
n = int(sys.stdin.readline().rstrip())
dp = [9999]*(n+5)
dp[3] = 1; dp[5] = 1

if n > 5:
    for i in range(6, n+1): #memoization
        dp[i] = min(dp[i-3], dp[i-5])+1

if dp[n] == 9999 or dp[n] == 10000:
    print(-1)
else:
    print(dp[n])