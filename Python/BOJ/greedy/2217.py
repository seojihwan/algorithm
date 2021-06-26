from sys import stdin
input = stdin.readline
n = int(input())
ans = 0
l = [int(input()) for _ in range(n)]
l.sort()
for e in l:
    ans = max(e * n, ans)
    n -= 1
print(ans)
