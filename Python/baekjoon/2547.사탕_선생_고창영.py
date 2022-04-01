from sys import stdin as st
test_case = int(st.readline().rstrip().rstrip())

for i in range(test_case):
    st.readline()
    students = int(st.readline().rstrip())
    sum = 0
    for j in range(students):
        sum += int(st.readline().rstrip())

    result = 'YES' if sum%students==0 else 'NO'
    print(result)