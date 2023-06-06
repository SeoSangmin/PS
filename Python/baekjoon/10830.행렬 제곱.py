from sys import stdin

input = stdin.readline

n, p = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def	matrix_mod(matrix, n, mod):
	for row in range(n):
		for col in range(n):
			matrix[row][col] %= mod
	return matrix

def	matrix_mul_mod(A, B, n, mod):
	result = [[] for _ in range(n)]
	num = 0
	for row in range(n):
		for col in range(n):
			for r in range(n):
				num += (A[row][r] * B[r][col]) % mod
			result[row].append(num % mod)
			num = 0
	return (result)

def	matrix_expo_mod(matrix, n, p, mod):
	result = []
	if (p == 1):
		return matrix_mod(matrix, n, mod)
	result = matrix_expo_mod(matrix, n, p//2, mod)
	result = matrix_mul_mod(result, result, n, mod)
	if (p % 2 == 0):
		return (result)
	result = matrix_mul_mod(result, matrix, n, mod)
	return (result)


result = matrix_expo_mod(matrix, n, p, 1000)

for i in range(n):
	for j in range(n):
		print(result[i][j], end=" ")
	print()
