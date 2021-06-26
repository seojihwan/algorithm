a = input()
b = input()
cnt = 0

s = 0
e = 0
while e <= len(a):
    print(a[s:e], s, e)
    if b in a[s:e]:
        cnt += 1
        s = e
    e += 1
print(cnt)
