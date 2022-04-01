from sys import stdin

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

res = []
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    gcd_ = gcd(a, b)
    res.append(str(a * b // gcd_)+'\n')

print(''.join(res))
    #최소공배수 == 두 자연수의 곱/최대공약수