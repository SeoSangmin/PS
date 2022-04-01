import sys
from sys import stdin as st
n, r = map(int, st.readline().split())

def C(n, r):
    ret = factorial(n) // (factorial(r) * factorial(n - r))
    return ret

memo_factorial = {1:1, 2:2}
# def factorial(x):
#     if x in memo_factorial:
#         return memo_factorial[x]
#     else:
#         ret = 1
#         for i in range(1, x + 1):
#             ret *= i
#         memo_factorial[x] = ret
#     return ret

def factorial(x):
    if x in memo_factorial:
        return memo_factorial[x]
    else:
        ret = factorial(x-1) * x
        memo_factorial[x] = ret
    return ret

# if __name__ == '__main__':
#     sys.setrecursionlimit(100000)
#     factorial(1)

print(C(n, r))




#1000000 1000 -> 개오래 걸림... 코드 메모이즘으로 수정하는 동안에도 안 끝나고 내 노트북 발열심해짐;