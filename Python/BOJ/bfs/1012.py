import sys
input = sys.stdin.readline

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = int(input())
res = []
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x]:
                q = [(y, x)]
                arr[y][x] = 0
                while q:
                    temp = []
                    for e in q:
                        ay, ax = e
                        for i in range(4):
                            dy = ay + d[i][0]
                            dx = ax + d[i][1]
                            if 0 <= dy < n and 0 <= dx < m and arr[dy][dx]:
                                temp.append((dy, dx))
                                arr[dy][dx] = 0
                    q = temp
                cnt += 1
    res.append(cnt)
for e in res:
    print(e)
