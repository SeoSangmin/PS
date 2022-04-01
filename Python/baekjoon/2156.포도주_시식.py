import sys
n = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(n+1)]

dp[1] = list[0]
if n > 1:
    dp[2] = dp[1] + list[1]

def run():
    if n == 1:
        return dp[1]
    if n == 2:
        return dp[2]
    for i in range(3, n+1):
        case1 = dp[i-3] + list[i-2] + list[i-1]
        case2 = dp[i-2] + list[i-1]
        case3 = dp[i-1]
        dp[i] = max(case1,
                    case2,
                    case3)
    return dp[n]

print(run())
