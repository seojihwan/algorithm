def check(a):
    for xx, yy, aa in a:
        if aa:
            if [xx + 1, yy - 1, 0] in a or [xx, yy - 1, 0] in a or ([xx + 1, yy, 1] in a and [xx - 1, yy, 1] in a):
                continue
            else:
                return False
        else:
            if not yy or [xx - 1, yy, 1] in a or [xx, yy, 1] in a or [xx, yy - 1, 0] in a:
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        if b:
            if a:
                if [x + 1, y - 1, 0] in answer or [x, y - 1, 0] in answer or ([x + 1, y, 1] in answer and [x - 1, y, 1] in answer):
                    answer.append([x, y, a])
            else:
                if not y or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                    answer.append([x, y, a])
        else:
            if not [x, y, a] in answer:
                continue
            answer.remove([x, y, a])
            if not(check(answer)):
                answer.append([x, y, a])

    answer = sorted(answer)
    return answer


n = [5, 5]
b = [[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]	, [[0, 0, 0, 1], [
    2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]	]


for i in range(2):
    solution(n[i], b[i])
