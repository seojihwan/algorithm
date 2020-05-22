import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

apt = []
cntArr = []
for _ in range(n):
    apt.append(list(map(int, list(input().rstrip("\n")))))

d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
cnt = 0

for y in range(n):
    for x in range(n):
        if apt[y][x]:
            cntApt = 1
            q = deque([(y, x)])
            apt[y][x] = 0
            while q:
                temp = []
                ay, ax = q.popleft()
                for i in range(4):
                    dy = ay + d[i][0]
                    dx = ax + d[i][1]

                    if 0 <= dy < n and 0 <= dx < n and apt[dy][dx]:
                        q.append((dy, dx))
                        apt[dy][dx] = 0
                        cntApt += 1
            cnt += 1
            cntArr.append(cntApt)

print(cnt)
for e in sorted(cntArr):
    print(e)
