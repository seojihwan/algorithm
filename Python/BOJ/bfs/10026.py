import sys
input = sys.stdin.readline

n = int(input())
grid = [input() for _ in range(n)]

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def check(mode: False, ca, cb):
    if mode:
        if ca == "R":
            if cb == "G":
                return True
        elif ca == "G":
            if cb == "R":
                return True
    if ca == cb:
        return True


def bfs(mode):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                q = [[y, x]]
                cnt += 1
                while q:
                    temp = []
                    for node in q:
                        ay, ax = node[0], node[1]
                        color = grid[ay][ax]
                        for i in range(4):
                            dy, dx = ay + d[i][0], ax + d[i][1]
                            if 0 <= dy < n and 0 <= dx < n:
                                if not visited[dy][dx] and check(mode, color, grid[dy][dx]):
                                    temp.append([dy, dx])
                                    visited[dy][dx] = 1
                    q = temp
    return cnt


print(bfs(0), bfs(1))
