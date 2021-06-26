def dfs(idx, v):
    global a
    global b
    if len(v) >= 2:
        if v[0] == '0':
            return
    if len(v) == 1:
        if a > idx:
            a = idx
            b = int(v)
            print(idx, b)
            return [idx, int(b)]
    l = len(v)
    for i in range(1, l):
        f = ''.join(v[:i])
        bb = ''.join(v[i:])
        if len(f) >= 2 and f[0] == '0':
            continue
        if len(bb) >= 2 and bb[0] == '0':
            continue
        dfs(idx + 1, str(int(f) + int(bb)))


def solution(n):
    n = str(n)

    global a
    global b
    a = 1000
    b = 1000
    dfs(0, n)
    answer = [a, b]
    return answer


n = 999999999
print(solution(n))
