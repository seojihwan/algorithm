from heapq import heappop as hpop, heappush as hpush


def solution(price):
    q = []
    d = [-1 for _ in range(len(price))]
    for idx, p in enumerate(price):
        hpush(q, (p, idx))
        while q and q[0][0] < p:
            e, i = hpop(q)
            d[i] = idx - i
    print(d)


solution([10 for _ in range(500000)])
