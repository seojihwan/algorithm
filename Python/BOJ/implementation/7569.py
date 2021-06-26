import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
t = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0
q = []
for iz, ez in enumerate(t):
    for iy, ey in enumerate(ez):
        for ix, ex in enumerate(ey):
            if ex == 1:
                q.append([iz, iy, ix])
while q:
    temp = []
    for node in q:
        z, y, x = node
        for az, ay, ax in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]:
            dz, dy, dx = z + az, y + ay, x + ax
            if 0 <= dx < m and 0 <= dy < n and 0 <= dz < h and not t[dz][dy][dx]:
                temp.append([dz, dy, dx])
                t[dz][dy][dx] = 1
    q = temp
    day += 1

for ez in t:
    for ey in ez:
        if 0 in ey:
            day = 0
print(day - 1)
