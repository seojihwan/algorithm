import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    y, x = map(int, input().split())
    arr[y].append(x)
    arr[x].append(y)
q = set()

for e in arr[1]:
    q.add(e)
    for el in arr[e]:
        q.add(el)
q.remove(1)
print(len(q))
