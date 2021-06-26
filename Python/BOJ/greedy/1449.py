import sys
input = sys.stdin.readline
n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if n == 1:
    print(1)
else:
    start = 0
    end = 1
    cnt = 1
    m = l
    while 1:
        if arr[end] - arr[start] + 1 <= m:
            end += 1
        else:
            m = l
            cnt += 1
            start = end
            end += 1
        if end == n:
            break
    print(cnt)
