import sys
input = sys.stdin.readline
n = int(input())

def isEndDay(n):
    isright = False
    if ('666' in str(n)):
        isright = True
    return isright

count = 1
temp = 666
while( count <= n ):
    while(True):
        if(isEndDay(temp)):
            temp += 1
            break
        else:
            temp += 1
    count += 1
print(temp-1)
