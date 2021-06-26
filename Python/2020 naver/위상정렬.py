from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    d = [0 for _ in range(n + 1)]
    dd = defaultdict(list)
    pp = defaultdict(list)
    for _ in range(k):
        x, y = map(int, input().split())
        dd[x].append(y)
        pp[y].append(x)
        d[y] += 1
    w = int(input())
    q = deque([])
    for idx, e in enumerate(d):
        if not e:
            q.append(idx)
    while q:
        node = q.popleft()
        pmax = 0
        for pe in pp[node]:
            pmax = max(pmax, cost[pe - 1])
        cost[node - 1] += pmax
        for el in dd[node]:
            d[el] -= 1
            if not d[el]:
                q.append(el)
    print(cost[w - 1])
