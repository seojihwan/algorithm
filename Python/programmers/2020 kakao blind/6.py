
from itertools import permutations as p


def solution(n, weak, dist):
    answer = 9
    dist = sorted(dist, reverse=True)
    for _ in range(len(weak)):
        for dd in list(p(dist, len(dist))):
            start, k = 0, 0
            for j in range(len(dd)):
                while k < len(weak) and weak[start] + dd[j] >= weak[k]:
                    k += 1
                start = k
                if start >= len(weak):
                    answer = min(answer, j + 1)
                    break

        weak[0] += n
        weak = sorted(weak)
    if answer == 9:
        answer = -1
    return answer


n, w, d = 12, [1, 3, 5, ], [1, 1]


n1, w1, d1 = 50, [1], [6]
print(solution(n, w, d))
# print(solution(n1, w1, d1))
