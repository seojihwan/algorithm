n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
err = False
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] and arr[i][k] and arr[k][j]:
                if arr[i][j] == arr[i][k] + arr[k][j]:
                    arr[i][j] = 0
                elif arr[i][j] > arr[i][k] + arr[k][j]:
                    err = True


for e in arr:
    ans += sum(e)
print(ans // 2 if not err else -1)
