a, b, v = map(int, input().split())
start, end = 0, v
while start < end:
    mid = (start + end) // 2
    if mid * (a - b) + a < v:
        start = mid + 1
    else:
        end = mid
print(start + 1)
