import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = [arr[0]]
for e in arr:
    pos = bisect_left(d, e)
    if d[-1] < e:
        d.append(e)
    else:
        d[pos] = e
print(len(d))
