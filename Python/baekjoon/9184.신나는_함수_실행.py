import sys
input = sys.stdin.readline
dict = {}
def w(a, b, c):
    if (a, b, c) in dict:
        return dict[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        dict[(a, b, c)] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        dict[(a, b, c)] = w(20, 20, 20)
        return dict[(a, b, c)]
    elif a < b and b < c:
        dict[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dict[(a, b, c)]
    else:
        dict[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dict[(a, b, c)]

a, b, c = map(int, input().split())

while((a, b, c) != (-1, -1, -1)):
    print("w({0}, {1}, {2}) = ".format(a, b, c) + str(w(a, b, c)))
    a, b, c = map(int, input().split())

