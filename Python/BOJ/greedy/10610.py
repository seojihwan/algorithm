import sys
input = sys.stdin.readline
n = list(input().rstrip('\n'))
n.sort()
if n[0] != "0":
    print(-1)
else:
    ans = ""
    t = 0
    for e in reversed(n):
        ans += e
        t += int(e)
    if t and t % 3 == 0:
        print(ans)
    else:
        print(-1)
