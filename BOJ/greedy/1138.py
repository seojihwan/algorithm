n = int(input())
arr = list(map(int, input().split()))
pos = [i for i in range(n)]
ans = [0 for _ in range(n)]
tmp = 1
for e in arr:
    ans[pos[e]] = tmp
    pos.pop(e)
    tmp += 1
print(*ans)
