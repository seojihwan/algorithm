n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
d = [0 for _ in range(100001)]

for coin in coins:
    d[coin] = 1


def dp(n):
    if d[n]:
        return d[n]
    d[n] = 100000000
    for coin in coins:
        if n - coin >= 1:
            d[n] = min(d[n], dp(n - coin) + 1)
    return d[n]


for i in range(k + 1):
    dp(i)
if d[k] != 100000000:
    print(d[k])
else:
    print(-1)
