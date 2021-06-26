from sys import stdin
input = stdin.readline
n, m, x = map(int, input().split())
INF = float('inf')
arr = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a - 1][b - 1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 0
                continue
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
ans = 0
for i in range(n):
    ans = max(ans, arr[i][x - 1] + arr[x - 1][i])
print(ans)
