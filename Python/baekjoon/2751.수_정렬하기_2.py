from sys import stdin as st
n = int(st.readline())
arr = [int(st.readline().rstrip()) for _ in range(n)]
arr.sort()
for i in arr:
    print(i)