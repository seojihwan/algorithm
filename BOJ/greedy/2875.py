n, m, k = map(int, (input().split()))
cnt = 0
if not n or not m:
    print(0)
else:
    while k and m:
        if n // m >= 2:
            n -= 1
        else:
            m -= 1
        k -= 1
    while n >= 2 and m >= 1:
        n -= 2
        m -= 1
        cnt += 1
    print(cnt)
