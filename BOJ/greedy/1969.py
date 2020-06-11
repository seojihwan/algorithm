import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
ans = ""
r = n * m
for i in range(m):
    d = dict()
    d["A"], d["T"], d["G"], d["C"] = 0, 0, 0, 0
    for j in range(n):
        d[arr[j][i]] += 1
    m = 0
    temp = ""
    for e in d:
        if m < d[e]:
            m = d[e]
            temp = e
        elif m == d[e]:
            if temp > e:
                temp = e
    r -= d[temp]
    ans += temp
print(ans)
print(r)
