from sys import stdin
from bisect import bisect_left as search
input = stdin.readline

n = int(input())
c = list(map(int, input().split()))
m = int(input())
d = list(map(int, input().split()))

c = sorted(c)

for de in d:
    print(search(c, de + 1) - search(c, de), end=' ')
