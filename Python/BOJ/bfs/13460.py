n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
blue, red = [], []
for y, r in enumerate(grid):
    for x, e in enumerate(r):
        if e == "B":
            blue = [y, x]
        if e == "R":
            red = [y, x]

ans = 11


def dfs(idx, blue, red, direction):
    global ans
    if idx == 11:
        return

    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if [dy, dx] != direction:
            ry, rx = red
            by, bx = blue
            rs, bs = False, False
            state = False
            while grid[ry + dy][rx + dx] != "#":
                state = True
                ry += dy
                rx += dx
                if grid[ry][rx] == "O":
                    rs = True
            while grid[by + dy][bx + dx] != "#":
                state = True
                by += dy
                bx += dx
                if grid[by][bx] == "O":
                    bs = True

            if [ry, rx] == [by, bx]:
                if red[0] < blue[0]:
                    if [dy, dx] == [1, 0]:
                        ry -= dy
                    elif [dy, dx] == [-1, 0]:
                        by -= dy
                elif red[0] > blue[0]:
                    if [dy, dx] == [1, 0]:
                        by -= dy
                    elif [dy, dx] == [-1, 0]:
                        ry -= dy
                elif red[1] < blue[1]:
                    if [dy, dx] == [0, 1]:
                        rx -= dx
                    elif [dy, dx] == [0, -1]:
                        bx -= dx
                elif red[1] > blue[1]:
                    if [dy, dx] == [0, 1]:
                        bx -= dx
                    elif [dy, dx] == [0, -1]:
                        rx -= dx

            if bs:
                continue
            if rs:
                ans = min(ans, idx + 1)
                return
            if state:
                dfs(idx + 1, [by, bx],
                    [ry, rx], [-dy, -dx])


dfs(0, blue, red, [0, 0])
if ans == 11:
    print(-1)
else:
    print(ans)
