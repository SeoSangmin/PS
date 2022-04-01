from sys import stdin as st

for _ in range(int(st.readline())):
    a, b = map(int, st.readline().split())
    a = a%10
    res = (a**b)%10
    print(res if res!=0 else 10 )