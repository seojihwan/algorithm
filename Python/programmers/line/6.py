from collections import defaultdict


def solution(companies, applicants):
    answer = []
    # while True:
    ta = []
    ca = []

    for e in applicants:
        ta.append(e.split(' '))
    for e in companies:
        ca.append(e.split(' '))

    for _ in range(2):
        c = defaultdict(list)
        for i, a in enumerate(ta):
            name, cop, num = a
            c[cop[0]].append(name)
            ta[i][1] = ta[i][1][1:]
        print(ta,c)
        for name, v, num in ca:
            num = int(num)
            cnt = 0
            for ev in v:
                if ev in c[name]:
                    cnt += 1
                    c[name].remove(ev)
                    if cnt == num:
                        break
    return answer


c = [["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]	, ["A abc 2", "B abc 1"]	]
a = [["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3",
      "e BCA 3", "f ABC 2"]	, ["a AB 1", "b AB 1", "c AB 1"]	]

for i in range(1):
    print(solution(c[0], a[0]))
