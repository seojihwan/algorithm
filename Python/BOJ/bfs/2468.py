import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for r in range(0, 101):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = []
    cnt = 0
    for y in range(n):
        for x in range(n):
            if grid[y][x] > r and not visited[y][x]:
                q.append((y, x))
                visited[y][x] = 1
                cnt += 1
                ans = max(ans, cnt)
                while q:
                    temp = []
                    for node in q:
                        ay, ax = node
                        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            yy, xx = ay + dy, ax + dx
                            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx] and grid[yy][xx] > r:
                                visited[yy][xx] = 1
                                temp.append((yy, xx))
                    q = temp
print(ans)
