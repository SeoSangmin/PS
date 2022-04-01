# 리스트를 사용하였음
#
# from sys import stdin as st
#
#stack = []
# for i in range(int(st.readline().rstrip())):
#     temp = str(input())
#     if ' ' in temp:
#         comm_item = temp.split()
#         stack.append(int(comm_item[1]))
#     elif temp == 'pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif temp == 'size':
#         print(len(stack))
#     elif temp == 'empty':
#         res = 1 if len(stack)==0 else 0
#         print(res)
#     elif temp == 'top':
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)








# 디큐를 사용하였음
from sys import stdin as st
from collections import deque

deque_list = deque()

for i in range(int(st.readline().rstrip())):
    temp = st.readline().split()
    if temp[0] == 'push':
        deque_list.append(int(temp[1]))
    elif temp[0] == 'pop':
        if len(deque_list)==0:
            print(-1)
        else:
            print(deque_list.pop())
    elif temp[0] == 'size':
        print(len(deque_list))
    elif temp[0] == 'empty':
        res = 1 if len(deque_list) == 0 else 0
        print(res)
    elif temp[0] == 'top':
        if len(deque_list) != 0:
            print(deque_list[-1])
        else:
            print(-1)