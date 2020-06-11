from collections import defaultdict
from sys import stdin
input = stdin.readline
di = defaultdict(lambda: defaultdict(int))
n = int(input())
for _ in range(n):
    y, x, p = input().strip().split()
    p = int(p)
    di[y][x] += p
    di[x][y] += p
start = "A"
end = "Z"

ans = 0
while 1:
    q = [start]
    back = defaultdict(int)
    visited = set()
    visited.add(start)
    flag = True
    while q and flag:
        temp = []
        for s in q:
            for e in di[s]:
                if di[s][e] > 0 and e not in visited:
                    temp.append(e)
                    visited.add(e)
                    back[e] = s
                    if e == end:
                        flag = False
                        break
        q = temp
    if end not in visited:
        break
    m = 1000000
    s, e = start, end
    while e != s:
        m = min(m, di[back[e]][e])
        e = back[e]
    ans += m
    s, e = start, end
    while e != s:
        di[back[e]][e] -= m
        di[e][back[e]] += m
        e = back[e]
print(ans)
