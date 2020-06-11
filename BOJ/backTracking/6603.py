import sys
from itertools import combinations
input = sys.stdin.readline
while 1:
    c = input().strip()
    if len(c) == 1 and not int(c):
        break
    c = c.split()
    c = c[1:]
    for e in combinations(c, 6):
        print(*e)
    print('')
