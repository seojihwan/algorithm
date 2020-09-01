import sys
input = sys.stdin.readline
r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
water = []
end = (-1, -1)
start = (-1, -1)
for y, e in enumerate(grid):
    for x, el in enumerate(e):
        if el == "*":
            water.append((y, x))
        elif el == "D":
            end = (y, x)
        elif el == "S":
            start = (y, x)
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = [start]
visited = [[0 for _ in range(c)] for _ in range(r)]
wvisited = [[0 for _ in range(c)] for _ in range(r)]
cnt = 0
while q:

    bb = []
    ww = []
    for wnode in water:
        wy, wx = wnode
        for i in range(4):
            awy = wy + d[i][0]
            awx = wx + d[i][1]
            if 0 <= awy < r and 0 <= awx < c and not wvisited[awy][awx] and grid[awy][awx] == "." and grid[awy][awx] != "X":
                ww.append((awy, awx))
                wvisited[awy][awx] = 1
                grid[awy][awx] = "*"
    for node in q:
        y, x = node
        if (y, x) == end:
            print(cnt)
            sys.exit()
        for i in range(4):
            ay = y + d[i][0]
            ax = x + d[i][1]
            if 0 <= ay < r and 0 <= ax < c and not visited[ay][ax] and grid[ay][ax] != "*" and grid[ay][ax] != "X":
                bb.append((ay, ax))
                visited[ay][ax] = 1
    water = ww
    q = bb
    cnt += 1
print("KAKTUS")
