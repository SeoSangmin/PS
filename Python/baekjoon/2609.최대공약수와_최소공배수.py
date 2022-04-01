from sys import stdin
a, b = map(int, stdin.readline().split())


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


gcd = gcd(a, b)
print('{}\n{}'.format(gcd, a*b//gcd))
#최소공배수 == 두 자연수의 곱/최대공약수

