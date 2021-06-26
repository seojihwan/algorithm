from collections import defaultdict


def solution(gems):
    answer = [1, len(gems)]
    gemset = set(gems)
    bag = defaultdict(int)

    s, e = 0, 0
    while e < len(gems):
        if len(bag) < len(gemset):
            bag[gems[e]] += 1
            e += 1
        else:
            if bag[gems[s]] == 1:
                del bag[gems[s]]
            else:
                bag[gems[s]] -= 1
            if answer[1] - answer[0] > e - s - 1:
                answer = [s + 1, e]
            s += 1
    return answer


gems = ["AA", "AB", "AC", "AA", "AC"]

solution(gems)
