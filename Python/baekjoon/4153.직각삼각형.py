from sys import stdin

def isright_angled_triange(a, b, c):
    isright = False
    list = [a, b, c]
    list.sort()
    if list[2]**2 == list[0]**2 + list[1]**2 :
        isright = True
    return isright

a, b, c = map(int, stdin.readline().split())
while a != 0:
    if isright_angled_triange(a, b, c) :
        print('right')
    else:
        print('wrong')
    a, b, c = map(int, stdin.readline().split())