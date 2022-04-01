from sys import stdin
n, m = map(int, stdin.readline().split())
cards = [i for i in map(int, stdin.readline().split())]

res = 0
t_res = 0
for i in cards:
    t_cards = cards[::]
    t_cards.remove(i)
    for j in t_cards:
        t_cards.remove(j)
        for k in t_cards:
            t_res = i + j + k
            if m >= t_res > res:
                res = t_res

print(res)

