n = input()
n = list(map(int, n))
d = [0]*10
for e in n:
    d[e] += 1
ans = 0
for idx, e in enumerate(d):
    if idx == 6 or idx == 9:
        continue
    ans = max(ans, e)
ex = d[6] + d[9]
ans = max(ans, ex // 2 + ex % 2)
print(ans)
