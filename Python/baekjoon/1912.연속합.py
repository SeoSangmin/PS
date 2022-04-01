#############분할 정복######################
from sys import stdin as st
import sys
MIN = -9223372036854775808 #-sys.maxsize -1
def fastMaxSum(array, low, high):
    global MIN
    #base case : 구간의 길이가 1일 경우
    if high==low: return array[low]

    #배열을 array[low ~ mid, array[mid+1 ~ high] 의 두 구간으로 나눈다.
    mid = (low + high)//2

    #두 부분에 모두 걸쳐 있는 최대 합 구간을 찾는다. 이 구간은
    #array[i ~ mid] 와 array[mid+1 ~ j] 형태를 갖는 구간의 합으로 이루어진다.

    #array[i ~ mid] 형태를 갖는 최대 구간을 찾는다 (분할된 구간 중 왼쪽에만 속하는 것들 중 최대를 찾는다)
    left = MIN #Max value of left side
    right = MIN #Max value of right side
    sum = 0
    for i in range(mid, low-1, -1):
        sum += array[i]
        left = max(left, sum)

    # array[mid+1 ~ j] 형태를 갖는 최대 구간을 찾는다 (분할된 구간 중 오른쪽에만 속하는 것들 중 최대를 찾는다)
    sum = 0
    for j in range(mid+1, high+1, 1):
        sum += array[j]
        right = max(right, sum)

    #최대 구간이 두 조각 중 하나에만 속해 있는 경우의 답을 재귀 호출로 찾는다
    single = max(fastMaxSum(array, low, mid), fastMaxSum(array, mid+1, high))

    #두 구간에 걸쳐서 있는 경우와 한 구간에만 속한 경우 중 큰 값을 반환한다.
    return max(left+right, single)

n = st.readline()
arr = [i for i in map(int, st.readline().split())]
res = fastMaxSum(arr, 0, len(arr)-1)
print(res)










#############DP##############
