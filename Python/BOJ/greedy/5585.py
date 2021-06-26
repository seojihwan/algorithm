n = int(input())
change = 1000 - n
c = [500, 100, 50, 10, 5, 1]
ans = 0
for e in c:
    if change // e >= 1:
        cnt = change // e
        change -= cnt * e
        ans += cnt
print(ans)
