import sys
n = int(sys.stdin.readline())

tri = [[int(i) for i in sys.stdin.readline().split()] for _ in range(n)]
results = [[-1 if i!=(n-1) else tri[i][j] for j in range(len(tri[i]))] for i in range(n)]

def dp(x, y):
    res = results[x][y]
    if res == -1:
        res += tri[x][y] + max(dp(x+1, y), dp(x+1, y+1)) +1
        results[x][y] = res
    return res

for i in range(n):
    for j in range(i+1):
        dp(i, j)

print(results[0][0])