from sys import stdin
n, m = map(int, stdin.readline().rstrip().split())

factorial_dp = {1:1, 2:2}
def factorial(x) -> int:
    if x in factorial_dp:
        return factorial_dp[x]
    res = 0
    for i in range(x):
        res = factorial(x-1) * x
    factorial_dp[x] = res
    return res

print(factorial(n) // (factorial(m) * factorial(n - m)))