import bisect
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
arr = list(int(input()) for _ in range(k))
# 경계조건인 hi 의 최대 값인 2**31 - 1이 답일 경우에는 오답처리 됨을 주의 hi 의 값을 2**31로 바꾸어서 이분탐색한다.
lo, hi = 0, 2**31
ans = 0
while lo < hi:
    mid = (lo + hi) // 2
    cnt = 0
    for e in arr:
        cnt += (e // mid)
    if cnt >= n:
        ans = max(ans, mid)
        lo = mid + 1
    else:
        hi = mid
print(ans)
