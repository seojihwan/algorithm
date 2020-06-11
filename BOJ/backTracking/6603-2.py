from sys import stdin
input = stdin.readline


def btr(li):
    if len(li) == 6:
        print(*li)
        return li
    for e in c:
        if not len(li):
            li.append(e)
            btr(li)
            li.pop()
        elif int(li[-1]) < int(e):
            li.append(e)
            btr(li)
            li.pop()


while 1:
    c = list(map(int, input().split()))
    if not c[0]:
        break
    c = c[1:]
    btr([])
    print('')
