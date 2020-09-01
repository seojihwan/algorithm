from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
lo, hi = 0, 2*10**9

ans = 0
while lo < hi:
    mid = (lo + hi) // 2
    sum = 0
    for e in arr:
        if e - mid > 0:
            sum += e - mid
    if sum < m:
        hi = mid

    else:
        ans = max(ans, mid)
        lo = mid + 1
print(ans)
