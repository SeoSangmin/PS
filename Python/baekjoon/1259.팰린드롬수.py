from sys import stdin as st

def isPal(str):
    isPal = True
    #검사 횟수는 문자열 길이//2
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            isPal = False
            break
    return isPal

x = st.readline().rstrip()
while x != '0':
    print('yes' if isPal(x) else 'no')
    x = st.readline().rstrip()