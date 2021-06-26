n = 5
g = [[1 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

# 시작점 (0,0)
q = [(0, 0)]
visited[0][0] = 1

while q:
    temp = []
    for node in q:
        y, x = node
        for ay, ax in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dy, dx = y + ay, x + ax
            if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and g[dy][dx]:
                visited[dy][dx] = 1
                temp.append((dy, dx))
                print(y, x)
    q = temp
