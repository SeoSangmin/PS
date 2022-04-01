from sys import stdin
def draw_star(n):
    global Array

    if n == 3: #base case
        Array[0][:3] = Array[2][:3] = ['*'] * 3
        Array[1][:3] = ['*', ' ', '*']
        return

    a = n // 3
    draw_star((a))
    for i in range(3):
        for j in range(3):
            for k in range(a):
                if i == 1 and j == 1:
                    Array[a * i + k][a * j:a * (j + 1)] = [' '] * a
                else:
                    Array[a * i + k][a * j:a * (j + 1)] = Array[k][:a]


n = int(stdin.readline().rstrip())
Array = [[0 for i in range(n)] for i in range(n)]
draw_star(n)
for i in Array:
    for j in i:
        print(j, end='')
    print()


# def concatenate(r1, r2):
#     return [''.join(x) for x in zip(r1, r2, r1)]
#
# def star10(n):
#     if n == 1:
#         return ['*']
#     n //= 3
#     x = star10(n)
#     a = concatenate(x, x)
#     b = concatenate(x, [' '*n]*n)
#
#     return a + b + a
#
# print('\n'.join(star10(int(input()))))


