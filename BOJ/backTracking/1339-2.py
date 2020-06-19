n = int(input())
l = []
s = []
d = [0] * 10
for _ in range(n):
    temp = input()
    for e in temp:
        if e not in s:
            s.append(e)
    l.append(temp)

limit = len(s)
ans = 0
t = [0]*10
r = [i for i in range(10)]


def dfs(idx):
    global ans
    if idx == limit:
        temps = 0
        for e in l:
            temp = 0
            for el in e:
                tt = d[s.index(el)]
                temp = temp * 10 + tt
            temps += temp
        ans = max(ans, (temps))
        return
    for i in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
        if not t[i]:
            d[idx] = i
            t[i] = 1
            dfs(idx + 1)
            t[i] = 0


dfs(0)
print(ans)
