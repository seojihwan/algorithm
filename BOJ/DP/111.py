t = int(input())
arr = []
d = [0 for _ in range(12)]
d[1] = 1
d[2] = 2
d[3] = 4


def dp(n):
    if d[n]:
        return d[n]
    d[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
    return d[n]


for _ in range(t):
    n = int(input())
    arr.append(dp(n))

for e in arr:
    print(e)
