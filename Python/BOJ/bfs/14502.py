
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline


def serachAll(arr, n, m):
    temp = 0
    stack = []
    virusStack = []
    for y in range(n):
        for x in range(m):
            if not arr[y][x]:
                stack.append([y, x])
            if arr[y][x] == 2:
                virusStack.append([y, x])
    stackCombination = list(combinations(stack, 3))
    for el in stackCombination:
        e = list(el)
        arr[e[0][0]][e[0][1]] = 1
        arr[e[1][0]][e[1][1]] = 1
        arr[e[2][0]][e[2][1]] = 1
        arr2 = deepcopy(arr)
        for ve in virusStack:
            virus(arr2, ve, n, m)
        temp = max(temp, check(arr2))

        arr[e[0][0]][e[0][1]] = 0
        arr[e[1][0]][e[1][1]] = 0
        arr[e[2][0]][e[2][1]] = 0
    return temp


tmp = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def virus(arr, vrs, n, m):
    y = vrs[0]
    x = vrs[1]
    for i in range(4):
        ay = y + tmp[i][0]
        ax = x + tmp[i][1]

        if 0 <= ay < n and 0 <= ax < m:
            if not arr[ay][ax]:
                arr[ay][ax] = 2
                virus(arr, [ay, ax], n, m)


def check(arr):
    cnt = 0
    for e in arr:
        for el in e:
            if not el:
                cnt += 1
    return cnt


n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
print(serachAll(arr, n, m))
