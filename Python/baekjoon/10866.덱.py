from sys import stdin as st
from collections import deque
n = int(st.readline())
deq = deque()

for i in range(n):
    str = st.readline().rstrip()
    res = 0
    if 'push_front' in str:
        deq.appendleft(str.split()[1])
    elif 'push_back' in str:
        deq.append(str.split()[1])
    elif str == 'pop_front':
        print(deq.popleft() if len(deq)!=0 else -1)
    elif str == 'pop_back':
        print(deq.pop() if len(deq) != 0 else -1)
    elif str == 'size':
        print(len(deq))
    elif str == 'empty':
        print(1 if len(deq) == 0 else 0)
    elif str == 'front':
        print(deq[0] if len(deq) != 0 else -1)
    elif str == 'back':
        print(deq[-1] if len(deq) != 0 else -1)