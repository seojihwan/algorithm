a = input()
b = input()
cnt = len(a) + len(b)
for ae in a:
    if ae in b:
        b = b.replace(ae, '', 1)
        cnt -= 2
print(cnt)
