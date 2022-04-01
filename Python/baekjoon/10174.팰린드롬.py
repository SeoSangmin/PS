import sys
input = sys.stdin.readline

for i in range(int(input())):
    st = input().lower().strip()

    print("Yes" if st == st[::-1] else "No")


from collections import deque
def isItPalindrome(string: str) -> bool:
    string = string.lower().rstrip().lstrip()
    deq = deque(string)
    while len(deq) > 1 :
        if deq.popleft() != deq.pop():
            return False
    return True

