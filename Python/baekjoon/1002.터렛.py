from sys import stdin
def dist(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    distance = ((x*x) + (y*y))**0.5
    return distance

def howManyIntersections(x1, y1, r1, x2, y2, r2):
    d = dist(x1, y1, x2, y2)
    if abs(r1-r2) > d:
        return 0
    elif d == abs(r1-r2) and r1 != r2:
        return 1
    elif abs(r1-r2) < d and d < r1+r2:
        return 2
    elif r1+r2 == d:
        return 1
    elif r1+r2 < d:
        return 0
    elif d==0 and r1 == r2:
        return -1

tc = int(stdin.readline().rstrip())
for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    print(howManyIntersections(x1,y1,r1,x2,y2,r2))
