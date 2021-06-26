def solution(n, horizontal):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    # 초기 좌표 왼쪽 상단
    # 초기 time = 0
    sy, sx, time = 0, 0, 0
    answer[sy][sx] = time
    # 초기 방향에 따라 움직임 설정
    direction = 'right'
    if horizontal:
        direction = 'right'
    else:
        direction = 'down'
    # 도착 지점에 도달할 때 까지 반복
    while not(sy == n - 1 and sx == n - 1):
        # 진행방향 별로 케이스 분리
        # 해당 진행방향에 맞게 이동
        # 이동 한 후 다음 진행방향 설정

        # 오른쪽으로 이동하는경우
        if direction == 'right':
            # 오른쪽으로 1만큼 이동
            # 시간 1만큼 추가
            sx += 1
            time += 1
            # 맨 꼭대기인 경우 아래 대각선으로 방향 변경
            if not sy:
                direction = 'downcross'
            # 바닥인 경우 위 대각선으로 방향 변경
            elif sy == n - 1:
                direction = 'upcross'

        # 아래로 내려가는 경우
        elif direction == 'down':
            # 아래로 1만큼 이동
            # 시간 1만큼 추가
            sy += 1
            time += 1
            # 왼쪽 열에 위치한 경우 위 대각선으로 방향 변경
            if not sx:
                direction = 'upcross'
            # 오른쪽 열에 위치한 경우 아래 대각선으로 방향 변경
            elif sx == n - 1:
                direction = 'downcross'

        # 위쪽 대각선으로 이동하는 경우
        elif direction == 'upcross':
            # 위로 한칸
            # 오른쪽으로 한칸
            # 시간 2만큼 추가
            sy -= 1
            sx += 1
            time += 2
            # 위쪽 열에 위치한 경우 오른쪽으로 방향 변경
            if not sy:
                direction = 'right'

            # 오른쪽 열에 위치한 경우 아래쪽으로 방향 변경
            # 위쪽 구석 인경우는 오른쪽이 아닌 아래쪽으로만 이동하기 때문에 elif이 아닌 if문으로 아래쪽 방향 후 처리함
            if sx == n - 1:
                direction = 'down'

        # 아래쪽 대각선으로 이동하는 경우
        elif direction == 'downcross':
            # 아래로 한칸
            # 왼쪽으로 한칸
            # 시간 2만큼 추가
            sy += 1
            sx -= 1
            time += 2
            # 왼쪽 열에 위치한 경우 아래쪽으로 방향 변경
            if not sx:
                direction = 'down'

            # 아래쪽 열에 위치한 경우 오른쪽으로 방향 변경
            # 왼쪽 + 아래쪽 구석인 경우 오른쪽으로만 이동하기 때문에 elif이 아닌 if문으로 오른쪽 방향 후처리
            if sy == n - 1:
                direction = 'right'
        # 이동한 sy, sx좌표를 통해
        # 도착 시간값 저장
        answer[sy][sx] = time
    return answer


n, h = 1, False
print(solution(n, h))
