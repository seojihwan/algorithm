n = int(input())
temp = n
p= 0
while 1 <= temp:
    p += 1
    temp /= 10

ans = 0
cnt = 1
for i in range(p - 1):
    ans += cnt * ((10 ** (i + 1)) - (10 ** i))
    cnt += 1
ans += cnt * (n - (10 ** (p - 1)) + 1)

print(ans)
