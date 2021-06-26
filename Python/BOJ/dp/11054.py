import sys
from bisect import bisect_left as bsl
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
u = [arr[0]]
ubnd = [0]
for i in range(1, n):
    m = bsl(u, arr[i])
    if u[len(u) - 1] < arr[i]:
        u.append(arr[i])
        ubnd.append(m)
    else:
        u[m] = arr[i]
        ubnd.append(m)

d = [arr[n - 1]]
dbnd = [0]
arr.reverse()
for i in range(1, n):
    m = bsl(d, arr[i])
    if d[len(d) - 1] < arr[i]:
        d.append(arr[i])
        dbnd.append(m)
    else:
        d[m] = arr[i]
        dbnd.append(m)

ans = 0
dbnd.reverse()
for i in range(n):
    ans = max(ans, ubnd[i] + dbnd[i])
print(ans + 1)
