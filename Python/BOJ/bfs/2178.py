import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 입력
# maze = [[0 for _ in range(m)] for _ in range(n)]
maze = []
for _ in range(n):
    maze.append(list(map(int, list(input().rstrip("\n")))))


# deque를 이용한 풀이
q = [(0, 0)]
maze[0][0] = 1
cnt = 1
while True:
    temp = []
    for node in q:
        y, x = node
        for move in d:
            if (0 <= y + move[0] < n) and (0 <= x + move[1] < m) and maze[y + move[0]][x + move[1]]:
                temp.append((y + move[0], x + move[1]))
                maze[y + move[0]][x + move[1]] = 0
                q = temp
    cnt += 1
    if (n - 1, m - 1) in temp:
        break

print(cnt)
