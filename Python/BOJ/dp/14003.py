import bisect
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

d = []
temp = []
d.append(arr[0])
temp.append([0, arr[0]])
for i in range(n):
    if d[len(d) - 1] < arr[i]:
        d.append(arr[i])
        temp.append([bisect.bisect_left(d, arr[i]), arr[i]])
    elif d[len(d) - 1] > arr[i]:
        m = bisect.bisect_left(d, arr[i])
        d[m] = arr[i]
        temp.append([m, arr[i]])
print(temp)
cnt = len(d) - 1
temp.reverse()
ans = []
for e in temp:
    if cnt == e[0]:
        ans.append(e[1])
        cnt -= 1
ans.reverse()
print(len(d))
print(*ans)
