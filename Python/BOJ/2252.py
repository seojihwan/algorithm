import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
d = dict()
s = [0] * (n + 1)
for e in range(m):
    a, b = map(int, input().split())
    s[b] += 1
    if a not in d.keys():
        d[a] = [b]
    else:
        d[a].append(b)
q = deque()
ans = []
for i in range(1, n + 1):
    if not s[i]:
        q.append(i)
while q:
    node = q.popleft()
    ans.append(node)
    if node in d.keys():
        for e in d[node]:
            s[e] -= 1
            if not s[e]:
                q.append(e)
print(*ans)
