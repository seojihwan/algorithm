n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
cnt = 0
coin.reverse()
while k > 0:
    for e in coin:
        if e <= k:
            x = 1
            if k // e >= 1:
                x = k // e
            k -= x * e
            cnt += x * 1
            break
print(cnt)
