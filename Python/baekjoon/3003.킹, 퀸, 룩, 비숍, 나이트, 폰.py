import sys
input = sys.stdin.readline

def solve():
	pieces = [1, 1, 2, 2, 2, 8]
	inputs = input().split()

	for idx, val in enumerate(pieces):
		print(val - int(inputs[idx]), end=" ")

solve()
