import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for e in arr:
    ans += sum(e)
ans /= 2
s = set()
for i in range(n):
    for j in range(n):
        if i < j:
            for k in range(n):
                if k != i and arr[k][j] < arr[i][j] and arr[k][j]:
                    temp = []
                    for m in range(2, n - 1):
                        temp += (list(combinations(arr[k], m)))
                    print(temp, arr[i][j])
                    for e in temp:
                        if sum(e) + arr[k][j] == arr[i][j]:
                            print("------", arr[i][j])
                            s.add(arr[i][j])
                            arr[i][j] = 0
                            arr[j][i] = 0
                            # ans -= arr[i][j]
                            break
print(s)
print(ans)
print(arr)
print(ans - sum(list(s)))
