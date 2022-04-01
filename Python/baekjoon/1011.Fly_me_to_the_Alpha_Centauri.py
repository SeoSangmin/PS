from sys import stdin
import math
def k(n):
    """
    :param n: distance
    :return: The minimum move number
    """
    max = int(math.sqrt(n))
    count = 0
    if max == math.sqrt(n):
        count = (max * 2) - 1
    elif max ** 2 < n <= max ** 2 + max:
        count = 2 * max
    else:
        count = (2 * max) + 1
    return count


test_case = int(stdin.readline().rstrip())
tests = []
for _ in range(test_case):
    x, y = map(int, stdin.readline().split())
    distance = y - x
    print(k(distance))
