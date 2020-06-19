import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = set(input().strip() for _ in range(n))
ans = []
for _ in range(m):
    b = input().strip()
    if b in a:
        ans.append(b)
print(len(ans))
for e in sorted(ans):
    print(e)    
