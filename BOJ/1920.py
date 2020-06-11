import sys
input = sys.stdin.readline
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = []
for e in b:
    if e in a:
        ans.append(1)
    else:
        ans.append(0)
for e in ans:
    print(e)
