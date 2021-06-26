from collections import deque


def solution(board):
    n = len(board)
    visited = [[1000000 for _ in range(n)] for _ in range(n)]
    ds = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    q = deque()
    q.append((0, 0, 0, -1))
    while q:

        y, x, c, t = q.popleft()
        if y == n - 1 and x == n - 1:
            continue
        for i in range(4):
            ay, ax = y + ds[i][0], x + ds[i][1]
            if 0 <= ay < n and 0 <= ax < n and not board[ay][ax]:
                if t == i or t == -1:
                    if visited[ay][ax] >= c + 100:
                        visited[ay][ax] = c + 100
                        q.append((ay, ax, c + 100, i))
                elif t != i:
                    if visited[ay][ax] >= c + 600:
                        visited[ay][ax] = c + 600
                        q.append((ay, ax, c + 600, i))
    answer = visited[n - 1][n - 1]
    return answer


board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
    0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
solution(board)
