from sys import stdin
def sieve(n): # 소수 리스트 반환
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    #print(s)
    for i in range(2, int(n**.5)+1):
        if s[i]: # i가 소수일 경우,
            s[i*2::i] = [0] * ((n - i)//i) # n-i 의 범위에서(i이상 n이하의 범위에서) i씩 증가하면서 i의 배수는 모두 제외시킨다.
    return [i for i, v in enumerate(s) if v] # s[i] 가 참인 경우 : i가 소수인 경우, i를 리스트에 추가

testcase = int(stdin.readline().rstrip())
for _ in range(testcase):
    even = int(stdin.readline().rstrip())
    half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
    nums = sieve(even)
    for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
        if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
            print(x, even-x)  # 작은수부터 출력
            break