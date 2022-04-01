# from sys import stdin
# xlist = []
# ylist = []
# for i in range(3):
#     x, y = map(int, stdin.readline().split())
#     if i != 3:
#         xlist.append(x)
#         ylist.append(y)
#
# if xlist[0] != xlist[1]:
#     x = xlist[0] if x!=xlist[0] else xlist[1]
#
# if ylist[0] != ylist[1]:
#     y = ylist[0] if y!=ylist[0] else ylist[1]
#
# print(f'{x} {y}')



from sys import stdin
x, y = map(int, stdin.readline().split())
x2, y2 = map(int, stdin.readline().split())
x3, y3 = map(int, stdin.readline().split())

if x2 != x3:
    x = x2 if x!=x2 else x3

if y2 != y3:
    y = y2 if y!=y2 else y3

print(f'{x} {y}')