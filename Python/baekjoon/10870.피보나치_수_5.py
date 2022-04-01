from sys import stdin
def fib(n):
    dict = {0:0, 1:1, 2:1}
    def nestedfib(n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = nestedfib(n-2)+nestedfib(n-1)
            return dict[n]
    return nestedfib(n)
print(fib(int(stdin.readline().rstrip())))