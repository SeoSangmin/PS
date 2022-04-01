from sys import stdin
numbers = stdin.readline().split()
print(sum([(int)(numbers[i])**2 for i in range(0, len(numbers))])%10)