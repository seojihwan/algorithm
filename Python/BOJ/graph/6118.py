import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[]for _ in range(n + 1)]

for _ in range(m):
    y, x = map(int, input().split())
    arr[y].append(x)
    arr[x].append(y)

visited = set()
visited.add(1)
q = [1]
d = 0
while len(visited) < n:
    temp = []
    while q:
        node = q.pop()
        for e in arr[node]:
            if e not in visited:
                temp.append(e)
                visited.add(e)
    q = temp
    d += 1
print(sorted(temp)[0])
print(d)
print(len(temp))
