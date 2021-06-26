import sys
b = [list(map(int, input().split())) for _ in range(9)]
c = {1, 2, 3, 4, 5, 6, 7, 8, 9}
pos = []
row = [[0 for _ in range(10)] for _ in range(10)]
col = [[0 for _ in range(10)] for _ in range(10)]
cro = [[0 for _ in range(10)] for _ in range(10)]


def cross(y, x):
    return 3 * (y // 3) + x // 3


for y, e in enumerate(b):
    for x, el in enumerate(e):
        col[x][el] = 1
        row[y][el] = 1
        cro[cross(y, x)][el] = 1
        if not el:
            pos.append((y, x))


def search(idx):
    if length == idx:
        for e in b:
            print(*e)
        sys.exit()
    y, x = pos[idx]
    for n in c:
        if not row[y][n] and not col[x][n] and not cro[cross(y, x)][n]:
            row[y][n], col[x][n], cro[cross(y, x)][n] = 1, 1, 1
            b[y][x] = n
            search(idx + 1)
            row[y][n], col[x][n], cro[cross(y, x)][n] = 0, 0, 0
            b[y][x] = 0


length = len(pos)
search(0)
