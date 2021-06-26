from itertools import combinations
from collections import defaultdict


def bs(a, x):

    s = 0
    e = len(a) - 1
    while s <= e:
        mid = (s + e) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            s = mid + 1
        else:
            e = mid - 1
        return -1


def isIn(o, e):
    cnt = 0

    for el in e:
        if bs(o, el) == -1:
            break
        cnt += 1

    return cnt, len(e)


def solution(orders, course):
    al = []
    aa = []
    temp = {}
    for e in orders:
        for alpha in e:
            if alpha not in al:
                al.append(alpha)
    al = sorted(al)
    comb = []
    for e in course:
        temp[e] = []
        comb.append((combinations(al, e)))

    for ec in comb:
        for e in ec:
            ii = isIn(orders, e)
            if ii[0] >= 2:
                temp[ii[1]].append([ii[0], e])
    for e in course:
        tt = sorted(temp[e], reverse=True)
        if len(tt):
            tmp = tt[0][0]
            for el in tt:
                print(el)
                if el[0] < tmp:
                    break
                aa.append(el[1])
    answer = []
    for e in aa:
        answer.append(''.join(e))
    answer = sorted(answer)
    return answer


o = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
     ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
c = [[2, 3, 4]	, [2, 3, 5]	, [2, 3, 4]]
for i in range(3):
    print(solution(o[i], c[i]))
