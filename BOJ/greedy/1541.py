from sys import stdin as st
input = st.readline
n = list(input())
ans = 0
temp = ""
b = 1
for e in n:
    if e == '-' or e == '+':
        ans += int(temp) * b
        temp = ""
        if e == '-':
            b = -1
    else:
        temp += e
ans += int(temp) * b
print(ans)
