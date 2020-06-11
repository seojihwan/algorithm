import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[10000000 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, p = map(int, input().split())
    arr[y - 1][x - 1] = min(p, arr[y - 1][x - 1])
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 0
                continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
for y, ey in enumerate(arr):
    for x, ex in enumerate(ey):
        if ex == 10000000:
            arr[y][x] = 0
for e in arr:
    print(*e)
