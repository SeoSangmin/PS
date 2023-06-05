from sys import stdin

input = stdin.readline();
a, b, c = map(int, input.split());

def	cal(a, b):
	tmp = 0;
	if (b == 0):
		return (1 % c)
	if (b == 1):
		return (a % c)
	tmp = cal(a, b//2)
	if (b % 2 == 0):
		return (tmp * tmp) % c
	return (tmp * tmp * a) % c

print(cal(a, b))
