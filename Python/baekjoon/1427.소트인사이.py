from sys import stdin

N_lst = list(stdin.readline().rstrip())
N_lst.sort(reverse=True)

for i in N_lst:
    print(i, end="")
