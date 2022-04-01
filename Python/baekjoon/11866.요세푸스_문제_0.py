from sys import stdin as st
from collections import deque
n, k = map(int, st.readline().split())

def Josephus(n, k):
    people = deque([str(i+1) for i in range(n)])
    ret = []
    while(len(people)!=0):
        people.rotate(-k+1)
        ret.append(people.popleft())
    return ret

res = Josephus(n, k)
print('<'+', '.join(res)+'>')