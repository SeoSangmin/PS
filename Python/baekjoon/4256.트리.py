
# n, preOrders, inOrders = int(input()), list(input().split()), list(input().split())
# in_loc = {v : i for i, v in enumerate(inOrders)}
# postOrders = []
# q = [[0, n-1, 0, n-1]]
# while q:
#     pstart, pend, istart, iend = q.pop()
#     root = preOrders[pstart]
#     inRootIdx = in_loc[root]
#     lsize = inRootIdx - istart
#     rsize = iend - inRootIdx
#     if inRootIdx < iend and lsize > 0: #when RHS exists
#         q.append([pstart + lsize + 1, pend, inRootIdx + 1, iend])
#
#     if inRootIdx > istart and lsize > 0: ##when LHS exists
#         q.append([pstart + 1, pstart + lsize, istart, inRootIdx - 1])
#
# print(' '.join(postOrders))

#----------------------------------------------------------------------
import sys
input = sys.stdin.readline


def dfs(pstart, pend, istart, iend):
    root = preOrders[pstart]
    inRootIdx = in_loc[root]
    lsize = inRootIdx - istart

    if inRootIdx > istart:
        dfs(pstart + 1, pstart + lsize, istart, inRootIdx - 1)
    if inRootIdx < iend:
        dfs(pstart + lsize + 1, pend, inRootIdx + 1, iend)
    postOrders.append(root)


t = int(input())
for i in range(t):
    n, preOrders, inOrders = int(input()), list(input().split()), list(input().split())
    in_loc = {v: i for i, v in enumerate(inOrders)}
    postOrders = []
    dfs(0, n - 1, 0, n - 1)
    print(' '.join(postOrders))