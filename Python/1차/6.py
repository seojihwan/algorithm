from collections import defaultdict
from itertools import permutations
# 함수 1: 커서 위치에서 타겟을 찾아가는 것 최단거리 반환


def find(b, y, x, t):
    visited = [[0 for _ in range(4)] for _ in range(4)]
    ty, tx = t
    q = [[y, x]]
    visited[y][x] = 1
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cnt = 0

    if [y, x] == t:
        return 1
    while q:
        temp = []
        for node in q:
            ny, nx = node
            for i in range(2):
                dy, dx = ny, nx
                while 0 <= dy < 4 and 0 <= dx < 4:
                    dy += d[i][0]
                    if 0 <= dy < 4 and 0 <= dx < 4:
                        if not visited[dy][dx]:
                            if b[dy][dx]:
                                visited[dy][dx] = 1
                                temp.append([dy, dx])
                                break
            for i in range(2):
                dy, dx = ny, nx
                while 0 <= dy < 4 and 0 <= dx < 4:
                    dx += d[i + 2][1]
                    if 0 <= dy < 4 and 0 <= dx < 4:
                        if not visited[dy][dx]:
                            if b[dy][dx]:
                                visited[dy][dx] = 1
                                temp.append([dy, dx])
                                break
            dy, dx = ny, nx
            for ay, ax in d:
                dy, dx = ny + ay, nx + ax
                if 0 <= dy < 4 and 0 <= dx < 4:
                    if not visited[dy][dx]:
                        visited[dy][dx] = 1
                        temp.append([dy, dx])
        q = temp
        cnt += 1
        if [ty, tx] in temp:
            return cnt + 1

    # 함수 2: 매칭되는 캐릭터를 찾아가는 것


def solution(board, r, c):
    al = set()
    cc = defaultdict(list)
    for y, ey in enumerate(board):
        for x, ex in enumerate(ey):
            if ex:
                al.add(ex)
                cc[ex].append([y, x])
    ol = (list(permutations(list(al), len(al))))

    def dfs(idx, pos, eol, cnt):
        y, x = pos
        ans = 1000000
        if idx == len(al):
            return cnt
        for i in range(2):
            s = find(board, y, x, cc[eol[idx]][i])
            yy = cc[eol[idx]][i][0]
            xx = cc[eol[idx]][i][1]
            m = find(board, yy, xx, cc[eol[idx]][(i + 1) % 2])
            board[y][x] = 0
            board[yy][xx] = 0
            ans = min(
                ans, dfs(idx + 1, cc[eol[idx]][(i + 1) % 2], eol, cnt + s + m))
            board[y][x] = eol[idx]
            board[yy][xx] = eol[idx]
        return ans
    answer = 1000000
    for eol in ol:
        answer = min(answer, dfs(0, [r, c], eol, 0))

    return answer


b = [[[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]	,
     [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]	]
r = [1, 0]
c = [0, 1]


# for i in range(2):
#     print(solution(b[i], r[i], c[i]))

print(solution(b[1], r[1], c[1]))
