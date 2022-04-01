#
# A, B, C = map(int,input().split())
#
# def BreakEventPoint(a, b, c):
#     """
#     N = 수량이라고 하자.
#     매출 = C * N
#     비용 = A + B * N
#     C*N > A+B*N 이 성립하는 가장 작은 N을 찾는 것이 목표, N은 자연수
#     C*N - B*N > A
#     N*(C-B) > A -> 이때 C-B <= 0 인 경우, 이 명제는 항상 거짓이므로 손익분기점은 없음. 즉 -1을 반환
#     C-B > 0 인 경우,
#     N > A / (C-B)
#     N >= A / (C-B) +1
#     가장 작은 N을 구해야하므로, N = A / (C-B) +1
#     :param a: 고정 비용
#     :param b: 가변 비용
#     :param c: 가격
#     :return: 손익분기점이 존재할 경우 - 손익분기점(수량)
#             손익분기점이 존재하지 않는 경우 - -1
#     """
#     if c <= b:
#         return -1
#     else:
#         return a // (c-b)+1
#
#
# print(BreakEventPoint(A, B, C))

a, b, c = map(int,input().split())
if c <= b :
    print(-1)
else :
    print(a // (c-b)+1)
