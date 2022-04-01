import sys
n = int(sys.stdin.readline())
dict = {}
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dict[a] = b
#lst = [ list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

for i in range(10):
    print(dict[i + 1]) if i + 1 in dict.keys재() else print("x")