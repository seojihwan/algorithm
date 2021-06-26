from collections import defaultdict


def solution(boxes):
    temp = 0
    d = defaultdict(int)
    for box in boxes:
        a, b = box
        d[a] += 1
        d[b] += 1
    for e in d:
        if d[e] >= 2:
            temp += d[e] // 2
    answer = len(boxes) - temp
    return answer


b = [[[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]	, [
    [1, 2], [3, 4], [5, 6]], [[1, 2], [2, 3], [3, 1]], [[1, 2], [1, 2], [1, 2], [1, 2]], [[1, 2], [1, 2], [1, 2]]
]

for i in range(5):
    print(solution(b[i]))
