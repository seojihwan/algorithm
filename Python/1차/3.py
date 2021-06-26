from collections import defaultdict


def lo(a, x):

    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo


def solution(info, query):

    inf = defaultdict(lambda:  defaultdict(
        lambda:  defaultdict(lambda:  defaultdict(list))))
    for e in info:
        e = e.split(' ')
        inf[e[0]][e[1]][e[2]][e[3]].append(int(e[4]))

    aa, bb, cc, dd = 3, 2, 2, 2
    xxx = ["cpp", "java", "python"]
    yyy = ["backend", "frontend"]
    www = ["junior", "senior"]
    zzz = ["chicken", "pizza"]

    for z in range(dd):
        for w in range(cc):
            for y in range(bb):
                for x in range(aa):
                    inf[xxx[x]][yyy[y]][www[w]][zzz[z]] = sorted(
                        inf[xxx[x]][yyy[y]][www[w]][zzz[z]])
    # print(inf["java"]["backend"]["junior"]["chicken"])
    answer = []
    for e in query:
        cnt = 0
        e = e.replace(' and', '').split(' ')
        aa, bb, cc, dd = 1, 1, 1, 1
        xxx = ["cpp", "java", "python"]
        yyy = ["backend", "frontend"]
        www = ["junior", "senior"]
        zzz = ["chicken", "pizza"]
        if e[0] == '-':
            aa = 3
        else:
            xxx = [e[0]]
        if e[1] == '-':
            bb = 2
        else:
            yyy = [e[1]]
        if e[2] == '-':
            cc = 2
        else:
            www = [e[2]]
        if e[3] == '-':
            dd = 2
        else:
            zzz = [e[3]]
        for z in range(dd):
            for w in range(cc):
                for y in range(bb):
                    for x in range(aa):
                        s = (inf[xxx[x]][yyy[y]][www[w]][zzz[z]])
                        cnt += len(s) - lo(s, int(e[4]))
        answer.append(cnt)
    return answer


i = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(i, q))
