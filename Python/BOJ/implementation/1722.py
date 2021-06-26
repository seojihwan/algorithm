import sys
n = int(input())
k = list(map(int, input().split()))

arr = [i for i in range(1, n + 1)]


def f(num):
    s = 1
    temp = 1
    while temp <= num:
        s *= temp
        temp += 1
    return s


i = f(n - 1)
if k[0] == 1:
    temp = k[1] - 1
    ans = []
    for t in range(n):
        i = f(n - t - 1)
        ans.append(arr[temp // i])
        arr.remove(arr[temp // i])
        temp -= ((temp // i) * i)
    for e in ans:
        print(e, end=" ")
else:
    ans = 0
    t = 0
    for e in k[1:]:
        i = f(n - t - 1)
        ans += arr.index(e) * i
        t += 1
        arr.remove(e)
    print(ans + 1)
