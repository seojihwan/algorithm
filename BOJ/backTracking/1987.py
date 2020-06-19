from copy import deepcopy as dc
r, c = map(int, input().split())
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
b = [input() for _ in range(r)]

ans = 0


s = [0]*26
s[ord(b[0][0]) - 65] = 1
q = [[0, 0, s, 1]]
while q:
    y, x, s, cnt = q.pop()
    ans = max(ans, cnt)
    for i in range(4):
        ay, ax = y + d[i][0], x + d[i][1]
        if 0 <= ay < r and 0 <= ax < c:
            pos = ord(b[ay][ax]) - 65
            if not s[pos]:
                s1 = dc(s)
                s1[pos] = 1
                q.append([ay, ax, s1, cnt + 1])

print(ans)
