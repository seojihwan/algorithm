def solution(n, delivery):

    answer = ['' for _ in range(n)]
    for _ in range(n // 2 + 100):
        for d in delivery:
            a, b, c = d
            a -= 1
            b -= 1
            if c:
                answer[a] = 'O'
                answer[b] = 'O'
            else:
                if answer[a] == 'O':
                    answer[b] = 'X'
                elif answer[b] == 'O':
                    answer[a] = 'X'

    for idx, e in enumerate(answer):
        if not e:
            answer[idx] = '?'
    answer = ''.join(answer)
    return answer
