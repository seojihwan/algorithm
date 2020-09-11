from collections import defaultdict


def ev(a, b):
    la = len(a)
    for i in range(la):
        if b[i] == '?':
            return 0
        elif a[i] < b[i]:
            return 1
        elif a[i] > b[i]:
            return -1


def up(w, d):
    s = 0
    e = len(w)
    while s < e:
        mid = (s + e)//2
        m = w[mid]
        if ev(m, d) == -1:
            e = mid
        else:
            s = mid + 1
    return s


def lo(w, d):
    s = 0
    e = len(w)
    while s < e:
        mid = (s + e)//2
        m = w[mid]
        if ev(m, d) == 1:
            s = mid + 1
        else:
            e = mid
    return s


def solution(words, queries):
    answer = []

    rwords = []
    for word in words:
        rwords.append(word[::-1])
    rwords = sorted(rwords)
    words = sorted(words)

    w = defaultdict(list)
    r = defaultdict(list)
    for word in words:
        w[len(word)].append(word)
    for rword in rwords:
        r[len(rword)].append(rword)
    for query in queries:
        if query[0] == '?':
            answer.append(
                up(r[len(query)], query[::-1]) - lo(r[len(query)], query[::-1]))

        else:

            answer.append(
                up(w[len(query)], query) - lo(w[len(query)], query))

    return answer


w, q = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	, [
    "fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(w, q))
