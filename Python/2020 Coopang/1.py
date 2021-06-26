def num(number, b):
    c = ""
    while number > 0:
        c = str(number % b) + c
        number = number // b
    temp = 1
    for ce in c:
        if ce == '0':
            continue
        temp *= int(ce)
    return [b, temp]


def solution(N):
    k, m = -1, -1
    for i in range(2, 10):
        a, b = num(N, i)
        if b > m:
            k, m = a, b
        elif b == m:
            if a >= k:
                k, m = a, b
    answer = [k, m]
    return answer


print(solution(1000000))
