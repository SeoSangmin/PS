import sys
test_case = int(sys.stdin.readline().rstrip())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(test_case)]

for i in range(test_case):
    temp = 1
    while list[i][2] > temp * list[i][0]:
        temp += 1
    print('{0}{1}'.format(str(list[i][0]*(1 - temp)+list[i][2]), temp if temp>=10 else str(0)+str(temp)))


# 백준 1등 코드
# import sys
# input = sys.stdin.readline
#
# for _ in range(int(input().rstrip())):
#     h,w,n = map(int,input().split())
#     print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0'))