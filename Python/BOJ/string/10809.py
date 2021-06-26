from sys import stdin
input = stdin.readline
l = input().strip()
length = len(l)
for i in range(26):
    if chr(97 + i) not in l:
        print(-1, end=' ')
        continue
    for idx, el in enumerate(l):
        if chr(97 + i) == el:
            print(idx, end=' ')
            break
