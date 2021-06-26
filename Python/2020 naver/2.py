
from collections import defaultdict


def solution(blocks):
    answer = []
    lev = len(blocks)
    al = defaultdict(lambda: defaultdict(int))
    for idx, e in enumerate(blocks):
        al[idx][e[0]] = e[1]
    s = 1
    while s < lev:
        temp = [blocks[s][0]]
        while len(temp) <= s:
            for i in range(s + 1):
                print(s, i)
                # 오른쪽 블록 존재: 부모 - 오른쪽
                if i not in temp:
                    if i + 1 in temp:
                        al[s][i] = al[s - 1][i] - al[s][i + 1]
                        temp.append(i)
                # 왼쪽 블록 존재: 부모(인덱스 - 1) - 왼쪽
                if i not in temp:
                    if i - 1 in temp:
                        al[s][i] = al[s - 1][i - 1] - al[s][i - 1]
                        temp.append(i)
            print(temp)
        s += 1
    answer = []
    for i in range(len(al)):
        for e in range(len(al[i])):
            answer.append(al[i][e])
    print(al)
    return answer


b = [[[0, 1], [2, 3]]]

for i in range(1):
    print(solution(b[0]))
