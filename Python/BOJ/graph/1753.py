from collections import defaultdict
from sys import stdin
from heapq import heappop as hpop, heappush as hpush
input = stdin.readline
v, e = map(int, input().split())
start = int(input())
ff = defaultdict(lambda: defaultdict(int))
for i in range(1, v + 1):
    if i == start:
        ff[start][i] = 0
        continue
    ff[start][i] = 10000000

for _ in range(e):
    a, b, w = map(int, input().split())
    if not ff[a][b] or ff[a][b] > w:
        ff[a][b] = w
pq = []
for e in ff[start]:
    hpush(pq, (ff[start][e], e))
while pq:
    w, node = hpop(pq)
    for e in ff[node]:
        if ff[start][e] > ff[start][node] + ff[node][e] and ff[node][e]:
            ff[start][e] = ff[start][node] + ff[node][e]
            hpush(pq, (ff[start][e], e))
for e in ff[start]:
    temp = ff[start][e]
    if temp == 10000000:
        print("INF")
    else:
        print(temp)
