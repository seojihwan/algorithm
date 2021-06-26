from collections import defaultdict
from sys import stdin
from heapq import heappop as hpop, heappush as hpush


def solution(n, ss, aa, bb, fares):
    s = [ss, aa, bb]
    ff = defaultdict(lambda: defaultdict(int))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                ff[i][j] = 0
                continue
            ff[i][j] = 10000000
    for a, b, w in fares:
        if not ff[a][b] or ff[a][b] > w:
            ff[a][b] = w
            ff[b][a] = w
    for i in range(3):
        start = s[i]
        pq = []
        for e in ff[start]:
            hpush(pq, (ff[start][e], e))
        while pq:
            w, node = hpop(pq)
            for e in ff[node]:
                if ff[start][e] > ff[start][node] + ff[node][e] and ff[node][e]:
                    ff[start][e] = ff[start][node] + ff[node][e]
                    hpush(pq, (ff[start][e], e))

    answer = 10000000
    for i in range(1, n + 1):
        answer = min(answer, ff[ss][i] + ff[aa][i] + ff[bb][i])
    return answer


n = [6, 7, 6]
s = [4, 3, 4]
a = [6, 4, 5]
b = [2, 1, 6]
f = [[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24],
      [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]	]


for i in range(1):
    print(solution(n[0], s[0], a[0], b[0], f[0]))
