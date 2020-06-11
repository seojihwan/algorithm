a, b = input().strip().split()
ra, rb = a[::-1], b[::-1]
if int(ra) > int(rb):
    print(ra)
else:
    print(rb)
