import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))

cent = set()


def find(e, idx):
    while idx < k:
        if e == arr[idx]:
            return idx
        idx += 1
    return 101


cnt = 0
for idx, e in enumerate(arr):
    if e not in cent:
        if len(cent) < n:
            cent.add(e)
        else:
            m = 0
            for el in cent:
                if el not in arr[idx:]:
                    cent.remove(el)
                    cnt += 1
                    m = 0
                    break
                m = max(find(el, idx), m)
            if m:
                cent.remove(arr[m])
                cnt += 1
            cent.add(e)


print(cnt)
