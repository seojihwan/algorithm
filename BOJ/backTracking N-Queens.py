from sys import exit  # exit함수, 수행시간 측정을 위한 library import
from time import time
n = int(input())
start = time()  # 시작 시간 저장


visited = [0] * n  # 열의 방문 여부 체크를 통해 해당 열의 중복을 확인
left_diagnols = [0] * (2*n - 1)  # 행과 열의 차이를 확인하여 해당 대각선(↖)의 중복을 확인
right_diagnols = [0] * (2*n - 1)  # 행과 열의 합을 확인하여 대각선(↗)의 중복을 확인


def drawBoard(q):   # 퀸들의 배치 정보를 입력받고, 보드의 모습을 출력해주는 함수
    board = [[" " for _ in range(n)] for _ in range(n)]
    for y, x in enumerate(q):  # 퀸들의 배치 정보에 따라 보드에 "Q"를 입력
        board[y][x - 1] = "Q"
    for e in board:  # 보드를 출력
        print(e)


def backTracking(q, idx):   # q 는 퀸들의 위치에 대한 정보, idx 는 입력할 idx번째 퀸
    if idx > n:  # n개의 퀸이 입력되었다면 보드를 그려주고 프로그램 종료
        drawBoard(q)
        print("12141718서지환 backTracking 수행시간:",
              round((time() - start) * 1000, 4), "ms")  # 현재시각 - 시작시간 = 수행 시간
        exit()  # 종료

    for e in range(1, n + 1):  # e의 범위는 1부터 n까지이다.
        # e번째 열을 사용 하지 않은경우 && ↖의 대각선 중복 X && ↗의 대각선 중복 X인 경우 계속해서 탐색
        if not visited[e - 1] and not left_diagnols[e - idx + n - 2] and not right_diagnols[e + idx - 3]:
            # 사용하였던 정보를 1로 바꾸어주고, 재귀호출 후에 0으로 바꾸어준다.
            visited[e - 1] = 1
            left_diagnols[e - idx + n - 2], right_diagnols[e + idx - 3] = 1, 1
            # 퀸의 배치 정보를 저장한 후 재귀호출 후, 삭제하여 backtracking이 이루어질 수 있도록 한다.
            q.append(e)
            # 저장된 퀸의 배치정보와, 다음에 입력해 줄 퀸의 위치는 idx + 1 을 backTracking함수에 전달
            backTracking(q, idx + 1)
            q.pop()
            visited[e - 1] = 0
            left_diagnols[e - idx + n - 2], right_diagnols[e + idx - 3] = 0, 0


# backTracking함수 호출
# 초기 퀸의 배치정보는 없으므로 [], 1번째 퀸을 입력해주기 위해 idx = 1
backTracking([], 1)
