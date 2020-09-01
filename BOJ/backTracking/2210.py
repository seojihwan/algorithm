arr = [input().strip().split() for _ in range(5)]
y, x = 0, 0
res = set()
temp = ""


def dfs(y, x, idx):
    global temp
    if idx == 6:
        res.add(temp)
        return
    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
        yy, xx = y + dy, x + dx
        if 0 <= yy < 5 and 0 <= xx < 5:
            tmp = temp
            temp += arr[yy][xx]
            dfs(yy, xx, idx + 1)
            temp = tmp


for i in range(5):
    for j in range(5):
        dfs(i, j, 0)
print(len(res))
