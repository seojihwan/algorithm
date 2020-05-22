from collections import deque
import sys
import time

input = sys.stdin.readline


def TOMATO(m: int, n: int):
    tomato, start = [], []
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 1:
                start.append((i, j))
        tomato.append(row)
    return tomato, start


def BFS(m: int, n: int, start: list, arr: list):
    queue = start
    time = 0
    while True:
        next_queue = []
        for i, j in queue:
            if 0 < i and arr[i-1][j] == 0:
                arr[i-1][j] = 1
                next_queue.append((i-1, j))
            if i < n-1 and arr[i+1][j] == 0:
                arr[i+1][j] = 1
                next_queue.append((i+1, j))
            if 0 < j and arr[i][j-1] == 0:
                arr[i][j-1] = 1
                next_queue.append((i, j-1))
            if j < m-1 and arr[i][j+1] == 0:
                arr[i][j+1] = 1
                next_queue.append((i, j+1))
        if not next_queue:
            break
        queue = next_queue
        time += 1

    for row in arr:
        for col in row:
            if col == 0:
                return -1
    return time


def BOJ7576():
    m, n = map(int, input().split())
    tomato, start = TOMATO(m, n)

    res = BFS(m, n, start, tomato)
    print(res)

start = time.time()  # 시작 시간 저장

BOJ7576()
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
