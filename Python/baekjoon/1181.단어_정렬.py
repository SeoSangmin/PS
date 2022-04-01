from sys import stdin as st

input_set = set([st.readline().rstrip() for _ in range(int(st.readline().rstrip()))])

max_value = max(len(i) for i in input_set) #입력된 글자들 중 가장 긴 글자의 글자수

result = []
for i in range(1,max_value+1):
    temp = [j for j in input_set if len(j) == i]
    temp.sort()
    result.extend(temp)

print("\n".join(result))











#----------------- 혹시라도? dict를 정렬할 때 사용 ---------------------#
# def item(x): #dict 정렬용
#     return x[1]
#
#
# sorted_dict = sorted(input_dict.items(), key=item)
