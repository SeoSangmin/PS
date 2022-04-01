n = int(input())
temp = input().split(' ')
del_node = int(input())
leaf = 0

def delete(temp, x):
    temp[x] = -2
    for i, v in enumerate(temp):
        if ( int(v)==x ):
            delete(temp, i)

delete(temp, del_node)

for i in range(len(temp)):
    isItLeaf = False
    if temp[i]==-2:
        continue
    for v in temp:
        if int(v) == i:
            isItLeaf = True
    if isItLeaf == False :
        leaf += 1

print(leaf)

