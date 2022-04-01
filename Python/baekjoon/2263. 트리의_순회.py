#-------------------------------------------------------------------------------------------
# # Using recursion
#
# import sys
# sys.setrecursionlimit(int(1e9))
# n = int(sys.stdin.readline())
# inOrders = list(map(int, sys.stdin.readline().split()))
# postOrders = list(map(int, sys.stdin.readline().split()))
#
# in_location=[0 for _ in range(n+1)]
# for i in range(n):
#     in_location[inOrders[i]]=i
#
# def dfs(inOrder, postOrder, i_s, i_e, p_s, p_e):
#     if p_e < p_s  or i_e < i_s:
#         return
#     root = postOrder[p_e]
#     inOrderRootidx = in_location[root]
#     size = inOrderRootidx - i_s
#
#     print(root, end=" ")
#     dfs(inOrder, postOrder, i_s, inOrderRootidx - 1, p_s, p_s + size - 1)
#     dfs(inOrder, postOrder, inOrderRootidx + 1, i_e, p_s + size, p_e - 1)
#
# dfs(inOrders, postOrders, 0, n-1, 0, n-1)


#-------------------------------------------------------------------------------------------
# Using stack frame and while iteration

import sys
sys.setrecursionlimit(9**9)
n, inOrders, postOrders = int(input()), list(input().split()), list(input().split())
in_loc = {v : i for i, v in enumerate(inOrders)}
preOrders = []
q = [[0, n-1, 0, n-1]]
while q:
    istart, iend, pstart, pend = q.pop()
    root = postOrders[pend]
    inRootIdx = in_loc[root]
    size = inRootIdx - istart
    preOrders.append(root)
    if inRootIdx < iend:
        q.append([inRootIdx + 1, iend, pstart + size, pend - 1])
    if inRootIdx > istart:
        q.append([istart, inRootIdx - 1, pstart, pstart + size - 1])

print(' '.join(preOrders))