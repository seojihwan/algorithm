import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
opos = []
epos = []
for y, e in enumerate(arr):
    for x, el in enumerate(e):
        if (y + x) % 2:
            opos.append((y, x))
        else:
            epos.append((y, x))


omax = 0
emax = 0
lchecked = [0] * 19
rchecked = [0] * 19


def odfs(start, idx):
    global omax
    omax = max(omax, idx)
    for e in opos[start:]:
        i, j = e
        start += 1
        if arr[i][j] and not lchecked[i - j + 9] and not rchecked[i + j]:
            arr[i][j] = 0
            lchecked[i - j + 9] = 1
            rchecked[i + j] = 1
            odfs(start, idx + 1)
            arr[i][j] = 1
            lchecked[i - j + 9] = 0
            rchecked[i + j] = 0


def edfs(start, idx):
    global emax
    emax = max(emax, idx)
    for e in epos[start:]:
        i, j = e
        start += 1
        if arr[i][j] and not lchecked[i - j + 9] and not rchecked[i + j]:
            arr[i][j] = 0
            lchecked[i - j + 9] = 1
            rchecked[i + j] = 1
            edfs(start, idx + 1)
            lchecked[i - j + 9] = 0
            rchecked[i + j] = 0
            arr[i][j] = 1


odfs(0, 0)
lchecked = [0] * 19
rchecked = [0] * 19
edfs(0, 0)

print(omax + emax)
