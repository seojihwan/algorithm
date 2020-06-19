from heapq import heappop as hpop, heappush as hpush
from collections import defaultdict
ff = defaultdict(lambda: defaultdict(int))
rr = defaultdict(int)
v, e = map(int, input().split())
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j:
            ff[i][j] = 1000000


rr = [1] * (v + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    ff[a][b] = c
pq = []
for e in ff[1]:
    hpush(pq, (ff[1][e], e))
while pq:
    c, node = pq.pop()
    for e in ff[1]:
        if ff[1][e] > ff[1][node] + ff[node][e]:
            ff[1][e] = ff[1][node] + ff[node][e]
            rr[e] = node
            hpush(pq, (ff[1][e], e))
print(ff[1])
red = ff[1][v]
start = v
visited = set()
while start != 1:
    ff[start][rr[v]] = 1000000
    visited.add(rr[v])
    start = rr[v]

pq = []
for e in ff[1]:
    hpush(pq, (ff[1][e], e))
while pq:
    c, node = pq.pop()
    for e in ff[1]:
        if e not in visited and node not in visited:
            if ff[1][e] > ff[1][node] + ff[node][e]:
                ff[1][e] = ff[1][node] + ff[node][e]
                rr[e] = node
                hpush(pq, (ff[1][e], e))
blue = ff[1][v]
print(ff[1])

print(red + blue)
