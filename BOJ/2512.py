import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

lo, hi = 1, max(arr) + 1
ans = 0
while lo < hi:
    mid = (lo + hi) // 2
    temp = 0
    for e in arr:
        if mid > e:
            temp += e
        else:
            temp += mid
    if temp > m:
        hi = mid
    else:
        lo = mid + 1
        ans = max(ans, mid)
print(ans)
