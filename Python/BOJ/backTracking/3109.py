import sys
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
ans = 0


def dfs(y, x):
    global ans
    if x == c - 1:
        ans += 1
        return True
    state = False
    for yy, xx in (y - 1, x + 1), (y, x + 1), (y + 1, x + 1):
        if 0 <= yy < r and arr[yy][xx] == '.':
            state = True
            arr[yy][xx] = 'x'
            if dfs(yy, xx):
                return True
    if not state:
        return False


for i in range(r):
    dfs(i, 0)
print(ans)
