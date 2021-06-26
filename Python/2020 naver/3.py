from collections import defaultdict, deque


def solution(n, edges):
    d = [0 for _ in range(n)]
    dd = defaultdict(list)
    cc = defaultdict(list)
    for edge in edges:
        a, b = edge
        dd[a].append(b)
        d[b] += 1

    q = [0]
    cnt = 0
    while q:
        temp = []
        for node in q:
            for el in dd[node]:
                d[el] -= 1
                if not d[el]:
                    temp.append(el)
                    cc[cnt].append(el)
        cnt += 1
        q = temp
    limit = len(cc)
    combs = []

    def dfs(arr, idx):
        if idx == limit:
            combs.append(arr)
        for ce in (cc[idx]):
            dfs(arr + [ce], idx + 1)
    dfs([], 0)
    answer = 100
    for comb in combs:
        q = [0]
        cnt = 1
        ccnt = 0
        while q:
            temp = []
            for node in q:
                for el in dd[node]:
                    if el != comb[ccnt]:
                        temp.append(el)
                        cnt += 1
            ccnt += 1
            q = temp
        answer = min(answer, cnt)
    return answer


n = [19, 14, 10]
edges = [[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]	,
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]], [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]		]
for i in range(3):
    print(solution(n[i], edges[i]))
