di = [0]*27
n = int(input())
for _ in range(n):
    for idx, e in enumerate(reversed(input())):
        di[ord(e) - 65] += 1 * pow(10, idx)
di = sorted(di, reverse=True)
ans = 0
cnt = 9
for e in di:
    if not e:
        break
    ans += cnt * e
    cnt -= 1
print(ans)
