import sys
n = int(input())
b = [0] * n

# def check ==        for i in range(1, (idx//2) + 1):
#                        if s[-i:] == s[-2*i:-i]: return False


def check(b, x):
    temp = 1
    while temp <= x // 2:
        start = 0
        while start + 2 * temp < x + 1:
            if(b[start:start + temp] == b[start + temp:start + 2 * temp]):
                return False
            start += 1
        temp += 1
    return True


def dfs(idx):
    if not check(b, idx):
        return
    if idx == n:
        print(''.join(list(map(str, b))))
        sys.exit()
    for i in range(1, 4):
        if b[-1] != i:
            b[idx] = i
            dfs(idx + 1)
            b[idx] = 0


dfs(0)
