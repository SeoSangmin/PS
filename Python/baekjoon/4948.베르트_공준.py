# from sys import stdin
# def sieve(n):
#     if n < 2:
#         return []
#     s = [0, 0] + [1] * (n - 1)
#     #print(s)
#     for i in range(2, int(n**.5)+1):
#         if s[i]: # i가 소수일 경우,
#             s[i*2::i] = [0] * ((n - i)//i) # n-i 의 범위에서(i이상 n이하의 범위에서) i씩 증가하면서 i의 배수는 모두 제외시킨다.
#     return [i for i, v in enumerate(s) if v] # s[i] 가 참인 경우 : i가 소수인 경우, i를 리스트에 추가
#
# inputs = []
# n = int(stdin.readline().rstrip())
# while(n!= 0):
#     inputs.append(n)
#     n = int(stdin.readline().rstrip())
# for i in range(len(inputs)):
#     li = sieve(inputs[i]*2)
#     print(len([j for j in li if j>inputs[i]]))
#


#Others
def getPrimaryNum_Eratos(N):
    nums = [True] * (N)
    for i in range(2, int(N**0.5) + 1):
        if nums[i] == True:
            for j in range(i+i ,N, i):
                nums[j] = False
    return [i for i in range(2, N) if nums[i] == True]

while True:
    N = int(input())
    if N == 0:
        break
    prime_list = getPrimaryNum_Eratos(2 * N + 1)
    answer_list = [num for num in prime_list if num > N]
    print(len(answer_list))