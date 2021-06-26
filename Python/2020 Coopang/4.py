from collections import defaultdict, deque


def solution(depar, hub, dest, roads):

    cc = defaultdict(list)
    mm = defaultdict(int)
    nn = defaultdict(int)

    check = defaultdict(int)
    for road in roads:
        a, b = road
        cc[a].append(b)

    q = [depar]
    check[depar] = 1
    while q:
        temp = []
        for node in q:
            for child in cc[node]:
                nn[child] += 1
                if not check[child]:
                    check[child] = 1
                    temp.append(child)
        q = temp
    # print(check)
    # print(nn)

    mm[depar] = 1
    q = deque([depar])
    while q:
        node = q.popleft()
        # print(node)
        for el in cc[node]:
            nn[el] -= 1
            mm[el] += mm[node]
            if not nn[el]:
                q.append(el)

    # print(mm)
    a1 = (mm[hub])
    cc = defaultdict(list)
    mm = defaultdict(int)
    nn = defaultdict(int)

    check = defaultdict(int)
    for road in roads:
        a, b = road
        cc[a].append(b)

    q = [hub]
    check[hub] = 1
    while q:
        temp = []
        for node in q:
            for child in cc[node]:
                nn[child] += 1
                if not check[child]:
                    check[child] = 1
                    temp.append(child)
        q = temp
    # print(check, "check")
    # print(nn)

    mm[hub] = 1
    q = deque([hub])
    while q:
        node = q.popleft()
        # print(node)
        for el in cc[node]:
            nn[el] -= 1
            mm[el] += mm[node]
            if not nn[el]:
                q.append(el)

    a2 = (mm[dest])
    print(a1,a2)
    answer = a1 * a2
    return answer


d = "ULSAN"
h = "SEOUL"
dd = "BUSAN"
r = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
print(solution(d, h, dd, r))
