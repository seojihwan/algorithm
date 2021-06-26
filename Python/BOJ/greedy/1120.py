a, b = input().split()
m = 50
la = len(a)
for i in range(len(b) - la + 1):
    cnt = 0
    for j in range(la):
        if a[j] != b[i + j]:
            cnt += 1
    if m > cnt:
        m = cnt
print(m)
