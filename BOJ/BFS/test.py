import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [i for i in range(n)]


def getParent(x):
    if p[x] == x:
        return x
    p[x] = getParent(p[x])
    return p[x]


def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


ans = set()
temp = []
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        temp.append([b, a])
    else:
        temp.append([a, b])
temp = sorted(temp)
for e in temp:
    unionParent(e[0] - 1, e[1] - 1)
for e in p:
    ans.add(e)
print(len(ans))
