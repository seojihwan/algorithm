n = int(input())
pos = []
cnt = 0


def check(e, li, idx):
    if e in li:
        return False
    for i, el in enumerate(li):
        if abs(el - e) == abs(i - idx):
            return False
    return True


def visit(li, idx):
    if idx == n:
        global cnt
        cnt += 1
        return
    for e in range(n):
        if check(e, li, idx):
            li.append(e)
            visit(li, idx + 1)
            li.pop()


visit(pos, 0)
print(cnt)
