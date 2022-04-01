# a, b, v = map(int,input().split())
# day = (v - a)//(a-b)
# if day == 0:
#     move = 0
# else:
#     move = v - a  # 총 이동 거리
# print('day:',day, ', move :',move)
# while move < v:
#     move += a
#     day += 1
#     if move >= v:
#         break
#     move -= b
#
# print(day)
# 999999900 = (v - a)//(a-b) == 날짜, (total)move = v - a
# 999999901

# from sys import stdin
# li = list(map(int, stdin.readline().split()))
# day_move = li[0] - li[1]
# target = li[2] - li[0]
# day = target // day_move
# move = day_move * day
# #print('day:',day, ', move :',move)
# while move < li[2]:
#     move += li[0]
#     day += 1
#     if move >= li[2]:
#         break
#     move -= li[1]
# print(day)

a, b, v = map(int,input().split())
day = (v - b) / (a - b)
print(int(day) if day == int(day) else int(day)+1)

