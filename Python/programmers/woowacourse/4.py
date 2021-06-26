def solution(n, board):
    answer = 0

    # 1번부터 n제곱 까지 순서대로 y,x좌표 저장
    pos = [[] for _ in range(n * n)]
    print(pos)
    for y, ey in enumerate(board):
        for x, ex in enumerate(ey):
            pos[ex - 1] = [y, x]
    print(pos)

    # 왼쪽 상단 시작
    sy, sx = 0, 0
    # i =>  0 ~ n 제곱 - 1
    for i in range(n * n):
        # 도착 지점
        dy, dx = pos[i]
        # 이동키 입력 수 + 엔터 입력
        cnt = 0
        print(sy, sx, dy, dx)
        # 시작 지점과 도착 지점의 차이의 절대값
        # 시작위치만 n 만큼 더해서 지름길 확인
        # 도착위치만 n 만큼 더해서 지름길 확인
        # y좌표 x 좌표에 대해 위 3가지중 최소 값을 더해줌
        cnt += min(abs(sy - dy), abs(n + sy - dy), abs(sy - (dy + n)))
        cnt += min(abs(sx - dx), abs(n + sx - dx), abs(sx - (dx + n)))
        # 엔터 누르면 + 1번
        cnt += 1
        print(cnt)
        answer += cnt
        # 시작 지점은 도착위치로 변경됨
        sy, sx = dy, dx
    print(answer)
    return answer


n, board = 3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
solution(n, board)
