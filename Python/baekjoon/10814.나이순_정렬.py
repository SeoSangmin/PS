from sys import stdin as st
tuples = []
for i in range(int(st.readline().rstrip())):
    age, name = map(str, st.readline().split())
    tuples.append((int(age), name))

sorted_list = sorted(tuples, key = lambda x:x[0])

for i in sorted_list:
    print(i[0],i[1])


# n_members = int(input())
#
# member_list = []
# for _ in range(n_members):
#     (x,y) = input().split()
#     member_list.append((int(x),y))
#
#
# sorted_list = sorted(member_list,key=lambda x: x[0])
#
# for i in sorted_list:
#     print(i[0], i[1])