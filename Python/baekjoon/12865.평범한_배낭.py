# import sys
# n, k = map(int, sys.stdin.readline().rstrip().split())
# w, v = [], []
# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
#
# for _ in range(n):
#     w_value, v_value = map(int, sys.stdin.readline().rstrip().split())
#     w.append(w_value)
#     v.append(v_value)
#
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if w[i-1] <= j:
#             dp[i][j] = max(dp[i-1][j-w[i-1]] + v[i-1], dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]
#
# print(dp[n][k])
#
# # def printDp():
# #     print("         0  1  2  3  4  5  6  7")
# #     for i in range(n + 1):
# #         print("물건 :", i, dp[i])
# #
# # printDp()




###-----------------------------------------------------
import sys
input=sys.stdin.readline
def sol():
    n,k=map(int,input().split())
    kk=k+1
    bag=dict()
    bag[0]=0
    data=[tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)
    for w,v in data:
        tmp={}
        for vv,ww in bag.items():
            if bag.get(vvv:=vv+v,kk)>(www:=w+ww):
                tmp[vvv]=www
        bag.update(tmp)
    print(max(bag.keys()))
sol()