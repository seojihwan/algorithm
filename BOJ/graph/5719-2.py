import sys
from heapq import heappop as hpop, heappush as hpush
from collections import defaultdict
input = sys.stdin.readline

ans = []
while 1:
    n, m = map(int, input().split())
    if not n and not m:
        break
    s, d = map(int, input().split())

    di = defaultdict(lambda: defaultdict(int))
    back = defaultdict(lambda: defaultdict(int))
    for _ in range(m):
        u, v, p = map(int, input().split())
        di[u][v] = p
        back[v][u] = p

    pq = []
    dp = [5000000] * n
    dp[s] = 0
    parent = [0] * n
    p = 0
    for e in di[s]:
        hpush(pq, (di[s][e], e))
    start, end = s, d
    while pq:
        for e in di[start]:
            if dp[e] > di[start][e] + p:
                dp[e] = di[start][e] + p
                hpush(pq, (dp[e], e))
        p, start = hpop(pq)
    q = [d]
    while q:
        end = q.pop()
        for e in back[end]:
            if dp[e] + back[end][e] == dp[end]:
                di[e][end] = 5000000
                q.append(e)
    pq = []
    dp = [5000000] * n
    dp[s] = 0
    parent = [0] * n
    p = 0
    for e in di[s]:
        hpush(pq, (di[s][e], e))
    start, end = s, d
    while pq:
        for e in di[start]:
            if dp[e] > di[start][e] + p:
                dp[e] = di[start][e] + p
                hpush(pq, (dp[e], e))
        p, start = hpop(pq)
    if dp[d] != 5000000:
        ans.append(dp[d])
    else:
        ans.append(-1)

for e in ans:
    print(e)
