import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = 0
for e in arr:
    if s + 1 < e:
        break
    else:
        s += e
print(s + 1)
