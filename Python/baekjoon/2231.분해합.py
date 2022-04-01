# from sys import stdin as st
#
# n = int(st.readline().rstrip())
# m = 1;
# if n==m:
#     print(0)
# else:
#     while (m < n):
#         temp = str(m)
#         #print('m=temp:',temp)
#         res = m
#         for i in range(0, len(str(m))):
#             res += int(temp[i])
#             #print('   i:', i, ', res:',res,'\n')
#         if(int(res)==n):
#             print(m)
#             break
#         m += 1
#         if(m>=n):
#             print(0)
#             break




#백준 시간 1등 코드
n = int(input())
for i in range(max(1, n-54),n):
    if sum(map(int,str(i)))+i == n:
        print(i)
        exit(0)
print(0)