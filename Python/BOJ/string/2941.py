a = input().strip()
print(list(a.count))
temp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for e in temp:
    a = a.replace(e, ' ')
print(len(a))
