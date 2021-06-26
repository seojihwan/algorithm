n = int(input())
d = [0 for _ in range(n)]

pp = list(int(input()) for _ in range(n))
d[0] = pp[0]
for i in range(1, n):
    if i == 1:
        d[1] = d[0] + pp[1]
    elif i == 2:
        d[2] = max(d[0], pp[1]) + pp[2]
    else:
        d[i] = max(d[i - 3] + pp[i - 1], d[i - 2]) + pp[i]
print(d[n - 1])
