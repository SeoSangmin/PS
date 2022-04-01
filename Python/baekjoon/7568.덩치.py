import sys
input = sys.stdin.readline
N = int(input())
arr = [input().strip().split(" ") for _ in range(N)]

def findRank(arr, cur):
    rank = 1
    for i in arr:
        if(int(i[0]) > int(cur[0]) and int(i[1]) > int(cur[1])):
            rank += 1
    return rank

for i in range(N):
    print(findRank(arr, arr[i]), end=' ')
