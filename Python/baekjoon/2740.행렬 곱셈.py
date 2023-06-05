from sys import stdin as st

n, m = map(int, st.readline().rstrip().split())
a = [list(map(int, st.readline().split())) for _ in range(n)]
m, k = map(int, st.readline().split())
b = [list(map(int, st.readline().split())) for _ in range(m)]
p = 0
for i in range(n):
	for j in range(k):
		for l in range(m):
			p += a[i][l] * b[l][j]
		print(p, end=" ")
		p = 0
	print()
