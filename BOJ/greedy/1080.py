import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().rstrip())))
for _ in range(n):
    b.append(list(map(int, input().rstrip())))

d = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            for k in range(9):
                y, x = i + d[k][0], j + d[k][1]
                if a[y][x]:
                    a[y][x] = 0
                else:
                    a[y][x] = 1
            cnt += 1
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            cnt = -1
print(cnt)
