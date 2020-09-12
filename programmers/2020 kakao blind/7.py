def turn(p1, p2, b, n):
    y1, x1 = p1
    y2, x2 = p2
    temp = []
    if y1 == y2:
        # y좌표 같고 축왼쪽
        # 위, 아래
        if 0 <= y1 - 1 < n and not b[y1 - 1][min(x1, x2)] and not b[y1 - 1][max(x1, x2)]:
            temp.append([[y1 - 1, min(x1, x2)], [y1, min(x1, x2)]])
        if 0 <= y1 + 1 < n and not b[y1 + 1][min(x1, x2)] and not b[y1 + 1][max(x1, x2)]:
            temp.append([[y1 + 1, min(x1, x2)], [y1, min(x1, x2)]])

        # 축 오른쪽
        if 0 <= y1 - 1 < n and not b[y1 - 1][min(x1, x2)] and not b[y1 - 1][max(x1, x2)]:
            temp.append([[y1 - 1, max(x1, x2)], [y1, max(x1, x2)]])
        if 0 <= y1 + 1 < n and not b[y1 + 1][min(x1, x2)] and not b[y1 + 1][max(x1, x2)]:
            temp.append([[y1 + 1, max(x1, x2)], [y1, max(x1, x2)]])

    else:
        # x좌표 같고 축위
        # 왼, 오
        if 0 <= x1 - 1 < n and not b[min(y1, y2)][x1 - 1] and not b[max(y1, y2)][x1 - 1]:
            temp.append([[min(y1, y2), x1 - 1], [min(y1, y2), x1]])
        if 0 <= x1 + 1 < n and not b[min(y1, y2)][x1 + 1] and not b[max(y1, y2)][x1 + 1]:
            temp.append([[min(y1, y2), x1], [min(y1, y2), x1 + 1]])

        # 축 아래
        if 0 <= x1 - 1 < n and not b[min(y1, y2)][x1 - 1] and not b[max(y1, y2)][x1 - 1]:
            temp.append([[max(y1, y2), x1 - 1], [max(y1, y2), x1]])
        if 0 <= x1 + 1 < n and not b[min(y1, y2)][x1 + 1] and not b[max(y1, y2)][x1 + 1]:
            temp.append([[max(y1, y2), x1], [max(y1, y2), x1 + 1]])

    return temp


def solution(board):
    answer = 0
    n = len(board)
    q = [[[0, 0], [0, 1]]]
    visited = [[[0, 0], [0, 1]]]
    while q:
        temp = []
        for node in q:
            p1, p2 = node
            y1, x1 = p1
            y2, x2 = p2
            for pos in turn(p1, p2, board, n):
                if not sorted(pos) in visited:
                    visited.append(sorted(pos))
                    temp.append(sorted(pos))
            for ay, ax in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dy1, dx1 = y1 + ay, x1 + ax
                dy2, dx2 = y2 + ay, x2 + ax
                if 0 <= dy1 < n and 0 <= dx1 < n and 0 <= dy2 < n and 0 <= dx2 < n:
                    if not board[dy1][dx1] and not board[dy2][dx2] and not sorted([[dy1, dx1], [dy2, dx2]]) in visited:
                        print([[dy1, dx1], [dy2, dx2]])
                        visited.append(sorted([[dy1, dx1], [dy2, dx2]]))
                        temp.append(sorted([[dy1, dx1], [dy2, dx2]]))
        q = temp
        answer += 1
        if [[n-1, n-2], [n - 1, n - 1]] in temp or [[n-2, n-1], [n - 1, n - 1]] in temp:
            break
    return answer
