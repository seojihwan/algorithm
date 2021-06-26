
import sys
import time


# 작업 코드


input = sys.stdin.readline

start = time.time()  # 시작 시간 저장

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

q = []
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            q.append((y, x))

d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
cnt = 0
while q:
    temp = []
    for y, x in q:
        for i in range(4):
            dy, dx = y + d[i][0], x + d[i][1]
            if 0 <= dy < n and 0 <= dx < m and not tomato[dy][dx]:
                tomato[dy][dx] = 1
                temp.append((dy, dx))
    q = temp
    if q:
        cnt += 1
for e in tomato:
    if 0 in e:
        cnt = -1
        break
print(cnt)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
