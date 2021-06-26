import sys
input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    temp.sort()
    m = 100001
    cnt = 0
    for e in temp:
        if m > e[1]:
            m = e[1]
            cnt += 1
    ans.append(cnt)
for e in ans:
    print(e)
