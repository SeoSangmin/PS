n = int(input())
diag = 1 #대각선 순서 == 대각선에서 제일 큰 숫자
count = 1 #해당 대각선까지의 모든 케이스 수
while count < n:
    diag += 1
    count += diag
if diag % 2 == 0:  # 짝수번째 대각선일 경우
    top = diag - count + n  # count - n == diff, diag - diff == top
    under = diag + 1 - top  # top + under = diag + 1
else:
    under = diag - count + n
    top = diag + 1 - under
print(f'{top}/{under}')