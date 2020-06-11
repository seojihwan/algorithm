n = int(input())
maxarr = [9 - i for i in range(n + 1)]
minarr = [i for i in range(n + 1)]
a = list(input().split())
for _ in range(n + 1):
    for idx, e in enumerate(a):
        if e == "<":
            if maxarr[idx] > maxarr[idx + 1]:
                maxarr[idx], maxarr[idx + 1] = maxarr[idx + 1], maxarr[idx]
            if minarr[idx] > minarr[idx + 1]:
                minarr[idx], minarr[idx + 1] = minarr[idx + 1], minarr[idx]
        elif e == ">":
            if maxarr[idx] < maxarr[idx + 1]:
                maxarr[idx], maxarr[idx + 1] = maxarr[idx + 1], maxarr[idx]
            if minarr[idx] < minarr[idx + 1]:
                minarr[idx], minarr[idx + 1] = minarr[idx + 1], minarr[idx]
    print(maxarr)
print(''.join(str(e) for e in maxarr))
print(''.join(str(e) for e in minarr))
