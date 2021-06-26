import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = set()
if n == k:
    print(0)
else:
    q = [(n)]
    cnt = 0
    while True:
        temp = set()
        for node in q:
            visited.add(node)
            if 0 <= node < k:
                temp.add((node + 1))
                temp.add((node - 1))
                temp.add((2 * node))
            elif k < node:
                temp.add((node - 1))
        cnt += 1
        if k in temp:
            break
        q = list(temp - visited)
    print(cnt)
