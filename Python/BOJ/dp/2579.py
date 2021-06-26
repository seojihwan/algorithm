n = int(input())
d = [0 for _ in range(n)]

pp = list(int(input()) for _ in range(n))
d[0] = pp[0]


def dp(idx):
    if idx < 0:
        return 0
    if d[idx]:
        return d[idx]
    d[idx] = max(dp(idx - 3) + pp[idx - 1],
                 dp(idx - 2)) + pp[idx]
    return d[idx]


print(dp(n - 1))
