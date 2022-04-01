from sys import stdin

list = stdin.readline().split()#음계들을 저장한 리스트

if list == [str(i) for i in range(1,9)]:
    print('ascending')
elif list == [str(i) for i in range(8,0,-1)]:
    print('descending')
else:
    print('mixed')