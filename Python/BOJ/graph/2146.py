n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

c = []
visited = [[0 for _ in range(n)]for _ in range(n)]
number = 0
for y in range(n):
    for x in range(n):
        if grid[y][x] and not visited[y][x]:
            number += 1
            q = [(y, x)]
            visited[y][x] = 1
            grid[y][x] = number
            while q:
                temp = []
                for node in q:
                    sy, sx = node
                    for ay, ax in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        dy, dx = ay + sy, ax + sx
                        if 0 <= dy < n and 0 <= dx < n and not grid[dy][dx]:
                            c.append((sy, sx))
                        if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and grid[dy][dx]:
                            temp.append((dy, dx))
                            visited[dy][dx] = 1
                            grid[dy][dx] = number
                q = temp
answer = 10000
for ce in c:
    visited = [[0 for _ in range(n)]for _ in range(n)]
    cnt = 0
    cy, cx = ce
    q = [(cy, cx)]
    visited[cy][cx] = 1
    while q:
        temp = []
        isfind = False
        for node in q:
            sy, sx = node
            for ay, ax in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                dy, dx = ay + sy, ax + sx
                if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and not grid[dy][dx]:
                    temp.append((dy, dx))
                    visited[dy][dx] = 1
                elif 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and grid[dy][dx] and grid[cy][cx] != grid[dy][dx]:
                    answer = min(answer, cnt)
                    isfind = True
                    break
            if isfind:
                break
        if isfind:
            break
        q = temp
        cnt += 1

print(answer)
