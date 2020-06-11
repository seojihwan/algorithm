import sys
from heapq import heappop, heappush
input = sys.stdin.readline

ans = []
while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    s, d = map(int, input().split())
    arr = [[500000 for _ in range(n)] for _ in range(n)]
    brr = dict()
    for i in range(n):
        brr[i] = []
    for _ in range(m):
        u, v, p = map(int, input().split())
        arr[u][v] = p
        brr[v].append([u, p])

    pq = []
    dp = [500000]*n
    dp[s] = 0
    heappush(pq, (0, s))
    while pq:
        cost, pos = heappop(pq)
        for idx, e in enumerate(arr[pos]):
            if cost + e < dp[idx]:
                dp[idx] = cost + e
                heappush(pq, (dp[idx], idx))
    q = [d]
    while q:
        end = q.pop()
        for idx, el in enumerate(brr[end]):
            if dp[end] == dp[el[0]] + el[1]:
                arr[el[0]][end] = 500000
                q.append(el[0])
    pq = []
    dp = [500000]*n
    dp[s] = 0
    heappush(pq, (0, s))
    while pq:
        cost, pos = heappop(pq)
        for idx, e in enumerate(arr[pos]):
            if cost + e < dp[idx]:
                dp[idx] = cost + e
                heappush(pq, (dp[idx], idx))
    if dp[d] == 500000:
        ans.append(-1)
    else:
        ans.append(dp[d])
for e in ans:
    print(e)
