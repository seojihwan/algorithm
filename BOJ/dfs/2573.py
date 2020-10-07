from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(n)]

year = 0
s = []
for y in range(n):
    for x in range(m):
        if ices[y][x]:
            s.append((y, x))
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    gcnt = 0
    bs = []
    for e in s:
        y, x = e
        if ices[y][x] and not visited[y][x]:
            gcnt += 1
            q = [(y, x)]
            visited[y][x] = 1
            while q:
                sy, sx = q.pop()
                for ay, ax in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    dy, dx = sy + ay, sx + ax
                    if 0 <= dy < n and 0 <= dx < m and not visited[dy][dx]:
                        if ices[dy][dx] > 0:
                            visited[dy][dx] = 1
                            q.append((dy, dx))
                        else:
                            if ices[sy][sx] > 0:
                                ices[sy][sx] -= 1
                if ices[sy][sx]:
                    bs.append((sy, sx))
    if not gcnt:
        print(0)
        break
    if gcnt >= 2:
        print(year)
        break
    year += 1
    s = bs
