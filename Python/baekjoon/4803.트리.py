import sys

def checking():
    return 0

while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    tree = [set() for _ in range(n+1)] # <set> can't be created by using only curly bracket with no item. ( {} -> it's dict type)
    print("\n---------------")
    for i in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        tree[v1].add(v2)
        tree[v2].add(v1)
    for i in range(1, n+1):
        print(tree[i])

    if n == 0 and m == 0:
        print("n, m are zero.")
        break
