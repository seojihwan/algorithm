def solution(v):
    answer = [0 for _ in range(3)]
    q = [(0, 0)]
    n = len(v)
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = [(i, j)]
                visited[i][j] = 1
                current = v[i][j]
                answer[current] += 1
                while q:
                    temp = []
                    for node in q:
                        y, x = node
                        for ay, ax in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            dy, dx = y + ay, x + ax
                            if 0 <= dy < n and 0 <= dx < n and not visited[dy][dx] and v[dy][dx] == current:
                                visited[dy][dx] = 1
                                temp.append((dy, dx))
                    q = temp

    return answer