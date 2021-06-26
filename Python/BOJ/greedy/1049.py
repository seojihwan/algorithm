import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
o = []

for _ in range(m):
    a, b = map(int, input().split())
    s.append(a)
    o.append(b)
six = min(s)
one = min(o)
if six >= one * 6:
    print(n * one)
else:
    print(min((n // 6 + 1) * six, (n // 6) * six + (n % 6) * one))
