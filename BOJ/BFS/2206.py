import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

q = [[0, 0, 0]]
visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 2
cnt = 1
ans = 10**6 + 1
while q:
    temp = []
    for node in q:

        y, x, b = node
        if y == n - 1 and x == m - 1:
            ans = cnt
            print(ans)
            sys.exit()
        for dy, dx in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ay, ax = y + dy, x + dx
            if 0 <= ay < n and 0 <= ax < m:
                if not b:
                    if grid[ay][ax]:
                        if visited[ay][ax] <= 1:
                            temp.append([ay, ax, b + 1])
                    else:
                        if visited[ay][ax] <= 1:
                            temp.append([ay, ax, b])
                    visited[ay][ax] = 2

                else:
                    if not grid[ay][ax] and not visited[ay][ax]:
                        temp.append([ay, ax, b])
                        visited[ay][ax] = 1
    q = temp
    cnt += 1
if ans == 10**6 + 1:
    print(-1)
