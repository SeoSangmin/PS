import sys

input = sys.stdin.readline

arr = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
	arr[i] = list(map(int, input().split()))

def parr():
	for i in range(9):
		print(arr[i])

def set_candi(i, j):
	candi_lst = [i for i in range(1, 10)]
	for col in range(9):
		if (arr[i][col] != 0 and (arr[i][col] in candi_lst)):
			print(arr[i][col])
			candi_lst.remove(arr[i][col])

	print("/")
	for row in range(9):
		if (arr[row][j] != 0 and (arr[row][j] in candi_lst)):
			print(arr[row][j])
			candi_lst.remove(arr[row][j])
	
	i -= i % 3
	j -= j % 3
	print(i, j)
	for row in range(3):
		for col in range(3):
			if (arr[row][col] != 0 and (arr[row][col] in candi_lst)):
				print(arr[row][col])
				candi_lst.remove(arr[row][col])
	return candi_lst

parr()
candi_lst = set_candi(1, 4)
print(candi_lst)

'''
def	check(i, j):
	if box_check(i - (i % 3), j - (j % 3)) == 0:
		return 0
	if row_check(i) == 0:
		return 0
	if col_check(j) == 0:
		return 0
	return 1

def	box_check(i, j):
	checked = [0 for _ in range(10)]
	for col in range(3):
import sys

input = sys.stdin.readline

arr = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
	arr[i] = list(map(int, input().split()))

def	check(i, j):
	if box_check(i - (i % 3), j - (j % 3)) == 0:
		return 0
	if row_check(i) == 0:
		return 0
	if col_check(j) == 0:
		return 0
	return 1

def	box_check(i, j):
	checked = [0 for _ in range(10)]
	for col in range(3):
		for row in range(3):
			if (arr[row][col] == 0):
				continue;
			if (checked[arr[row][col]] == 0):
				checked[arr[row][col]] = 1
			else:
			 	return (0)
	return (1);

def	col_check(j):
	checked = [0 for _ in range(10)]
	for row in range(9):
		if (arr[row][j] == 0):
			continue;
		if (checked[arr[row][j]] == 0):
			checked[arr[row][j]] = 1
		else:
			return (0)
	return (1);


def	row_check(i):
	checked = [0 for _ in range(10)]
	for col in range(9):
		if (arr[i][col] == 0):
			continue;
		if (checked[arr[i][col]] == 0):
			checked[arr[i][col]] = 1
		else:
			return (0)
	return (1);

def print_arr():
	for i in range(9):
		for j in range(9):
			print(arr[i][j], end=" ")
		print();

#main func
def recursive(i, j):
	if j == 9 and i == 8:
		print_arr()
		return ;
	elif j == 9:
		j = 0;
		i += 1;
	if (arr[i][j] != 0):
		recursive(i, j + 1);
	else:
		for value in range(1, 10):
			arr[i][j] = value;
			if (check(i, j) == 1):
				recursive(i, j + 1)
			else:
				arr[i][j] = 0;

recursive(0, 0);		for row in range(3):
			if (arr[row][col] == 0):
				continue;
			if (checked[arr[row][col]] == 0):
				checked[arr[row][col]] = 1
			else:	
			 	return (0)
	return (1);

def	col_check(j):
	checked = [0 for _ in range(10)]
	for row in range(9):
		if (arr[row][j] == 0):
			continue;
		if (checked[arr[row][j]] == 0):
			checked[arr[row][j]] = 1
		else:
			return (0)
	return (1);


def	row_check(i):
	checked = [0 for _ in range(10)]
	for col in range(9):
		if (arr[i][col] == 0):
			continue;
		if (checked[arr[i][col]] == 0):
			checked[arr[i][col]] = 1
		else:
			return (0)
	return (1);

def print_arr():
	for i in range(9):
		for j in range(9):
			print(arr[i][j], end=" ")
		print();

#main func
def recursive(i, j):
	if j == 9 and i == 8:
		print_arr()
		return ;
	elif j == 9:
		j = 0;
		i += 1;
	if (arr[i][j] != 0):
		recursive(i, j + 1);
	else:
		for value in range(1, 10):
			arr[i][j] = value;
			if (check(i, j) == 1):
				recursive(i, j + 1)
			else:
				arr[i][j] = 0;

recursive(0, 0);

'''
