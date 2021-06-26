from heapq import heappop as hpop, heappush as hpush
from collections import defaultdict
from sys import stdin
input = stdin.readline
n, m, x = map(int, input().split())

ff = defaultdict(lambda: defaultdict(int))
rr = defaultdict(lambda: defaultdict(int))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            ff[i][j] = 1000000
            rr[i][j] = 1000000

for _ in range(m):
    a, b, t = map(int, input().split())
    ff[a][b] = t
    rr[b][a] = t
pq = []
for e in ff[x]:
    hpush(pq, (ff[x][e], e))
while pq:
    t, node = hpop(pq)
    for e in ff[x]:
        if ff[x][e] > ff[x][node] + ff[node][e]:
            ff[x][e] = ff[x][node] + ff[node][e]
            hpush(pq, (ff[x][e], e))
pq = []
for e in rr[x]:
    hpush(pq, (rr[x][e], e))
while pq:
    t, node = hpop(pq)
    for e in rr[x]:
        if rr[x][e] > rr[x][node] + rr[node][e]:
            rr[x][e] = rr[x][node] + rr[node][e]
            hpush(pq, (rr[x][e], e))
ans = 0
for i in range(1, n + 1):
    ans = max(ans, ff[x][i] + rr[x][i])
print(ans)
