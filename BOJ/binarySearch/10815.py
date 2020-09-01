import bisect
import sys
input = sys.stdin.readline
n = int(input())
c = list(map(int, input().split()))
m = int(input())
d = list(map(int, input().split()))

c = sorted(c)
ans = []


def search(e):
    lo, hi = 0, len(c)
    while lo < hi:
        mid = (lo + hi) // 2
        if c[mid] > e:
            hi = mid
        elif c[mid] < e:
            lo = mid + 1
        else:
            ans.append('1')
            return
    ans.append('0')


for de in d:
    search(de)
print(*ans)
