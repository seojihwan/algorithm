from collections import defaultdict


def solution(k, score):
    d = defaultdict(int)
    m = defaultdict(set)
    r = set()
    for i in range(len(score)):
        if i + 1 < len(score):
            d[score[i] - score[i + 1]] += 1
            m[score[i] - score[i + 1]].add(i)
            m[score[i] - score[i + 1]].add(i + 1)

    for key in d:
        if d[key] >= k:
            for el in m[key]:
                r.add(el)
    if not len(r):
        return 0
    else:
        return len(score) - len(r)



k = 2
s = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]	
print(solution(k, s))
