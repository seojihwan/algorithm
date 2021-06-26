s = input().strip()
d = dict()
c = 3
for i in range(26):
    if not (i % 3) and 0 < i <= 15 or i == 19 or i == 22:
        c += 1
    d[chr(65 + i)] = c
cnt = 0
for e in (s):
    cnt += d[e]
print(cnt)
