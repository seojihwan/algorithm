

# t : 0 아래 1 오른쪽 2 위 3 왼쪽
def solution(maze):
    n = len(maze)
    temp = []
    temp.append([1 for _ in range(n + 2)])
    for e in maze:
        temp.append([1] + e + [1])
    temp.append([1 for _ in range(n + 2)])
    maze = temp

    def check(t, pos):      # 참이면 해당 방향에 벽이 있다.
        y, x = pos
        if t == 0:
            y, x = y + 1, x

        elif t == 1:
            y, x = y, x + 1

        elif t == 2:
            y, x = y - 1, x

        elif t == 3:
            y, x = y, x - 1

        return maze[y][x]

    answer = 0

    pos = [1, 1]
    t = 0
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 방향에 맞는 전진
    cnt = 0
    while pos != [n, n]:
        if not check((t + 1) % 4, pos):  # 벽이 없다 왼쪽에
            if pos == [1, 5]:
                print(pos, t)
            t = (t + 1) % 4
            py, px = pos
            ty, tx = d[t]
            if pos == [1, 5]:
                print(pos, t)
            if 0 <= py + ty < n + 2 and 0 <= px + tx < n + 2:
                pos = [py + ty, px + tx]
        elif not check(t, pos):  # 벽이 없다 앞에
            py, px = pos
            ty, tx = d[t]
            if 0 <= py + ty < n + 2 and 0 <= px + tx < n + 2:
                pos = [py + ty, px + tx]

        elif not check((t - 1) % 4, pos):  # 벽이 없다 오른쪽에
            t = (t - 1) % 4
            py, px = pos
            ty, tx = d[t]
            if 0 <= py + ty < n + 2 and 0 <= px + tx < n + 2:
                pos = [py + ty, px + tx]

        elif not check((t - 2) % 4, pos):  # 벽이 없다 뒤에만
            t = (t - 2) % 4
            py, px = pos
            ty, tx = d[t]
            if 0 <= py + ty < n + 2 and 0 <= px + tx < n + 2:
                pos = [py + ty, px + tx]

        answer += 1
        cnt += 1
    return answer


m = [[[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]	,
     [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [
         0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]	,
     [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [
         0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]	,
     [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]	]


for i in range(1):
    print(solution(m[1]))
