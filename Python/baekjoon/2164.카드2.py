from sys import stdin as st
n = int(st.readline().rstrip())
temp = 1
while(temp < n):
    temp *= 2

print(temp if temp==n else 2*n - temp)



# n,s=int(input()),1
# while s<n:
#     s*=2
# print(s if s==n else 2*n-s)