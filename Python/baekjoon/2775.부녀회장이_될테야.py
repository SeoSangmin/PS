import sys
import time

testcase = int(sys.stdin.readline().rstrip())
kk = []
nn = []
for i in range(testcase):
    kk.append(int(sys.stdin.readline().rstrip()))
    nn.append(int(sys.stdin.readline().rstrip()))

d = {}
for i in range(14):
    d[(0, i + 1)] = i + 1
    d[(1, i + 1)] = (i + 2) * (i + 1) // 2

def eff_hmp(k, n):
    ans = 0
    if (k, n) in d:
        return d[(k, n)]
    else:
        for i in range(1, n + 1):
            ans += eff_hmp(k - 1, i)
        d[(k, n)] = ans
        return ans

start = time.time()  # 시작 시간 저장
for i in range(testcase):
    print(eff_hmp(kk[i], nn[i]))

print(f"time elapsed : {round(int((time.time() - start)*1000), 0)}") #ms
