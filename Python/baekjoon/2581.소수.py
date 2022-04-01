# from sys import stdin
#
# def isPrime(n):
#     isPrime = True
#     if n==1: return False
#     elif n==2: return True
#     elif n%2 == 0: return False
#     else:
#         d = 3
#         while d*2 <= n:
#             if n%d == 0:
#                 isPrime = False
#                 break
#             d += 2
#         return isPrime
#
# m = int(stdin.readline().rstrip());n = int(stdin.readline().rstrip())
# sum = 0;min = 10001
# for i in range(m, n+1):
#     if isPrime(i) == True:
#         if min==10001:min = i
#         sum += i
# if sum != 0:print(sum);print(min)
# else:print(-1)


# from sys import stdin
# def isPrime(n):
#     isPrime = True
#     if n==1: return False
#     elif n==2: return True
#     elif n%2 == 0: return False
#     else:
#         d = 3
#         while d*2 <= n:
#             if n%d == 0:
#                 isPrime = False
#                 break
#             d += 2
#         return isPrime
# m = int(stdin.readline().rstrip());n = int(stdin.readline().rstrip());sum = 0;min = 10001
# for i in range(m, n+1):
#     if isPrime(i) == True:
#         if min==10001:min = i
#         sum += i
# if sum != 0:print(sum);print(min)
# else:print(-1)






"""
다른 사람이 만든 에라토스테네스 체를 구현한 알고리즘.
새로 알게된 것 : 리스트를 슬라이싱하면 기본적으로 시퀀스 자료형이 되며, \
            슬라이싱한 상태에서 자료의 갯수만 맞게 연속된 자료형을 할당해주면,\
            원래 리스트의 슬라이싱된 인덱스의 값들만 바뀌게 되고\
            새로운 리스트는 생성되지 않는다.
"""
def sieve(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    print('s length:',len(s))
    #print(s)
    for i in range(2, int(n**.5)+1):
        if s[i]: # i가 소수일 경우,
            s[i*2::i] = [0] * ((n - i)//i) # n-i 의 범위에서(i이상 n이하의 범위에서) i씩 증가하면서 i의 배수는 모두 제외시킨다.
    return [i for i, v in enumerate(s) if v] # s[i] 가 참인 경우 : i가 소수인 경우, i를 리스트에 추가

n = int(input())
print(sieve(n))
