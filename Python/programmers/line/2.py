from collections import deque


def solution(ball, order):

    w = deque([])
    ball = deque(ball)
    answer = []
    for o in order:
        if o == ball[0]:
            answer.append(o)
            ball.popleft()
            while True:
                if len(ball) and ball[0] in w:
                    w.remove(ball[0])
                    answer.append(ball[0])
                    ball.popleft()
                else:
                    break

        elif o == ball[-1]:
            answer.append(o)
            ball.pop()
            while True:
                if len(ball) and ball[-1] in w:
                    w.remove(ball[-1])
                    answer.append(ball[-1])
                    ball.pop()
                else:
                    break
        else:
            w.append(o)
    return answer


b = [[1, 2, 3, 4, 5, 6]	, [11, 2, 9, 13, 24]]
o = [[6, 2, 5, 1, 4, 3]	, [9, 2, 13, 24, 11]	]


for i in range(2):
    print(solution(b[i], o[i]))


[11, 2, 9, 13, 24]
[11, 2, 9]
