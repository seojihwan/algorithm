t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
d = [[0, 0] for _ in range(41)]
d[1] = [0, 1]
d[2] = [1, 1]


def dp(n):
    if n == 0:
        return [1, 0]
    if d[n][0] or d[n][1]:
        return d[n]
    d[n] = [dp(n - 1)[0] + dp(n - 2)[0], dp(n - 1)[1] + dp(n - 2)[1]]
    return d[n]


ans = []
for e in arr:
    ans.append(dp(e))

for e in ans:
    print((e[0]), (e[1]))
