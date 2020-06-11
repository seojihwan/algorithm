import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())
j = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(k)]
j = sorted(j)
b = sorted(b)
q = []
start = 0
ans = 0
for eb in b:
    while start < n:
        if eb >= j[start][0]:
            heappush(q, (-j[start][1], j[start][1]))
            start += 1
        else:
            break
    if q:

        ans += heappop(q)[1]
print(ans)
