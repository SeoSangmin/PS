# from sys import stdin as st
# n = int(st.readline())
# dp = [0 for _ in range(1000001)]
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) %15746
#
# print(dp[n])

#---------------------------------------------------
# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
# n = int(input())
# dict = {1: 1, 2: 2}
# def dp(n):
#     if n in dict:
#         return dict[n]
#     dict[n] = dp(n-1) + dp(n-2)
#     return dict[n]
#
# print(dp(n)%15746)
#--------------------------------------------------- others for time checking
# 어느 변태의 풀이
def mul(a, b):
    return (
        (a[0]*b[0]+a[1]*b[2]) % 15746,
        (a[0]*b[1]+a[1]*b[3]) % 15746,
        (a[2]*b[0]+a[3]*b[2]) % 15746,
        (a[2]*b[1]+a[3]*b[3]) % 15746
    )

def foo(n):
    a, b = (1,1,1,0), (1,0,0,1)
    while n > 0:
        if n & 1: #1이랑 &비트 연산 해서 1(True)나오려면, 홀수여야함. 즉, 홀수인 경우를 따지는 조건임
            b = mul(a, b)
        n >>= 1 #나누기2한 것과 거의 같은 효과
        a = mul(a, a)
    return b[0]

res = foo(int(input()))
print(f"{res}")