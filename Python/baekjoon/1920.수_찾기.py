"""
맨 처음에 in 연산자를 활용하여 풀면 안 되나? 싶어서 리스트에 값을 저장하고 풀어봤다. 하지만!! 시간초과가 났다.
그래서 이분탐색으로 문제를 풀고 다른 사람들의 것을 확인했더니, 처음 내가 짠 코드와 거의 유사했다!(이분탐색x)
이러한 결과는 list의 in/not in 연산의 시간복잡도와 set의 in/not in 연산의 시간복잡도 차이에서 기인한다.
list의 in/not in 연산의 시간복잡도는 O(N)인 반면, set의 해당 연산의 시간복잡도는 O(1)로 상수시간이다.
(참고로, dictionary의 in/not in 연산 또한 O(1)이다. + 이분탐색의 시간복잡도는 O(logN)

+ dictionary와 set은 둘 다 해쉬 구조이기 때문에 빠른 것.
다만 set은 key는 없고 value만 있는 것이라고 생각하면 된다.
"""
######이분 탐색(binary search)를 이용한 풀이 - 시간 오래 걸림
from sys import stdin as st
n = int(st.readline().rstrip())
n_list = [i for i in map(int, st.readline().split())]
n_list.sort()

m = int(st.readline().rstrip())
m_list = [i for i in map(int, st.readline().split())]

for i in m_list:
    low = 0
    high = n - 1
    middle = n // 2
    while (high - low) != 1:
        if n_list[low] <= i < n_list[middle]:
            high = middle
        elif n_list[middle] <= i < n_list[high]:
            low = middle
        else:
            break
        middle = low + (high - low) // 2

    res = 1 if (i == n_list[low]) or (i == n_list[high]) else 0
    print(res)
################################################################


# ## 파이썬의 기본 자료구조 연산을 이용한 풀이 - 시간 빠름
# from sys import stdin as st
# n, n_list, m = int(st.readline().rstrip()), set(st.readline().split()), int(st.readline().rstrip())
#
# res = 0
#
# for i in st.readline().split():
#     res = 1 if i in n_list else 0
#     print(res)
