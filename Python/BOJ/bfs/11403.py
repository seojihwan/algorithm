n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    d = ['0'] * n
    q = [i]
    visited = [0] * n
    while q:
        temp = []
        for node in q:
            for x, el in enumerate(arr[node]):
                if el and not visited[x]:
                    d[x] = '1'
                    visited[x] = 1
                    temp.append(x)
        q = temp
    print(*d)
