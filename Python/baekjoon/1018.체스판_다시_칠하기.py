from sys import stdin
n, m = map(int, stdin.readline().split())
Map = [[j for j in list(stdin.readline().rstrip())] for i in range(n)]

#비교할 체스판 두 경우를 2차원 리스트로 생성해준다.
b = ['W' if i%2!=0 else 'B' for i in range(8)]
w = ['B' if i%2!=0 else 'W' for i in range(8)]
black = [b, w]*4
white = [w, b]*4

b = 0
w = 0
count = []
for i in range(0, n-7):
    for j in range(0, m-7):
        for k in range(8):
            for h in range(8):
                if Map[i+k][j+h] != black[k][h]:
                    b += 1
                if Map[i+k][j+h] != white[k][h]:
                    w += 1
        count.append(b); b = 0
        count.append(w); w = 0

print(min(count))