import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sol = 0
for e in arr:
    sol += e * n
    n -= 1
print(sol)
