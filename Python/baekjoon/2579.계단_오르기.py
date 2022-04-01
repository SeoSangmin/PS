import sys

n = int(sys.stdin.readline().rstrip())
score = []
for i in range(n):
    score.append(int(sys.stdin.readline().rstrip()))
if len(score)<3:
    score.append(0)
    score.append(0)
sum = [0]*(n+3)

sum[0] = score[0]
sum[1] = max(score[0] + score[1], score[1])
sum[2] = max(score[0]+score[2], score[1]+score[2]);

for i in range(3, n):
    sum[i] = max(sum[i-2]+score[i], sum[i-3] + score[i-1] + score[i])

print(sum[n-1])
