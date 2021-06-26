from collections import defaultdict
from sys import stdin
input = stdin.readline
parent = defaultdict(int)
depth = defaultdict(int)
lines = defaultdict(list)
n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

q = [1]
visited = [0 for _ in range(n + 1)]
visited[1] = 1
cnt = 1
while q:
    temp = []
    for node in q:
        for line in lines[node]:
            if not visited[line]:
                parent[line] = node
                depth[line] = cnt
                temp.append(line)
                visited[line] = 1
    q = temp
    cnt += 1


def findCommonParent(n1, n2):
    if depth[n2] < depth[n1]:
        n1, n2 = n2, n1
    cnt = depth[n2] - depth[n1]
    for _ in range(cnt):
        n2 = parent[n2]

    while True:
        if n1 == n2:
            return n1
        n2 = parent[n2]
        n1 = parent[n1]


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(findCommonParent(a, b))
