l, c = map(int, input().split())
a = input().split()
a.sort()
a = ''.join(a)

ans = []

temp = ['a', 'e', 'i', 'o', 'u']


def check(li):
    cnt = 0
    for e in li:
        for el in temp:
            if e == el:
                cnt += 1
    if 0 < cnt and 1 < l - cnt:
        return True
    return False


def b(li, idx):
    if idx == l and check(li):
        ans.append(''.join(li))
        return
    for e in a:
        if len(li) and li[-1] >= e:
            continue
        li += e
        b(li, idx + 1)
        li.pop()


b([], 0)
for e in ans:
    print(e)
