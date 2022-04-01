from sys import stdin
x, y, w, h = map(int, stdin.readline().split())
list = [x, y, h-y, w-x]
list.sort()
print(list[0])

