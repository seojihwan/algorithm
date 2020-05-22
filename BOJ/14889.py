import sys
import itertools
input = sys.stdin.readline
n = int(input())
arr = [i for i in range(n)]
ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))
c = list(itertools.combinations(arr, n // 2))
cnt = len(c) // 2
d = sorted(c, reverse=True)
c = c[:cnt]
d = d[:cnt]
ans = 100000
for i in range(cnt):
    start = 0
    link = 0
    for j in range(n // 2):
        for k in range(n // 2):
            if j != k:
                start += ab[c[i][j]][c[i][k]]
                link += ab[d[i][j]][d[i][k]]
    ans = min(ans, abs(start - link))
print(ans)
