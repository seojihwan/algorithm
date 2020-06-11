n, m = map(int, input().split())

if m == 1 or n == 1:
    print(1)
elif m <= 4:
    if n == 2:
        print(1 + (m - 1) // 2)
    else:
        print(m)
elif m <= 6:
    if n == 2:
        print(3)
    else:
        print(4)
else:
    if n == 2:
        print(4)
    else:
        print(m - 2)
