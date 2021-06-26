from collections import deque
n = int(input())
arr = list(map(int, input().split()))
root = []
c = [[] for _ in range(n)]
for i in range(n):
    if arr[i] != -1:
        c[arr[i]].append(i)
    else:
        root.append(i)


def leafCnt(root):
    cnt = 0
    q = deque([])
    q += root
    while q:
        root = q.popleft()
        if c[root]:
            q += c[root]
        else:
            cnt += 1
    return cnt


r = int(input())
if arr[r] != -1:
    c[arr[r]].remove(r)
else:
    c[r] = []
    root.remove(r)
print(leafCnt(root))
