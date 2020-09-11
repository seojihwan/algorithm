def solution(key, lock):
    n = len(key)
    m = len(lock)

    def rotate(y, x, size):
        a = size // 2
        y -= a
        x -= a
        y, x = x + a, -y + a
        if not (size % 2):
            x -= 1
        return [y, x]

    def check(k, l, ym, xm):
        for y in range(m):
            for x in range(m):
                yy, xx = y + ym, x + xm
                if 0 <= yy < n and 0 <= xx < n:
                    if (key[yy][xx] and lock[y][x]) or (not key[yy][xx] and not lock[y][x]):
                        return False
                else:
                    if not lock[y][x]:
                        return False
        return True
    for ym in range(-m, m + 1):
        for xm in range(-m, m + 1):
            for _ in range(4):
                temp = []
                for y, ykey in enumerate(key):
                    for x, xkey in enumerate(ykey):
                        if xkey:
                            yy, xx = rotate(y, x, n)
                            key[y][x] = 0
                            temp.append([yy, xx])
                for e in temp:
                    yy, xx = e
                    key[yy][xx] = 1
                if(check(key, lock, ym, xm)):
                    return True
    return False


k, l = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	, [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(k, l))
