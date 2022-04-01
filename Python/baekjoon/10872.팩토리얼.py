from sys import stdin

def facto(n):
    return 1 if n==0 else facto(n-1)*n

print(facto(int(stdin.readline().rstrip())))
