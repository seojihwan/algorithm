def solution(numbers, hand):
    answer = ''
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    left = 10
    right = 12
    for e in numbers:
        if e == 1 or e == 4 or e == 7:
            answer += 'L'
            left = e
        elif e == 3 or e == 6 or e == 9:
            answer += 'R'
            right = e
        else:
            ld = abs((left - 1) % 3 - (e - 1) % 3) + \
                abs((left - 1) // 3 - (e - 1) // 3)
            rd = abs((right - 1) % 3 - (e - 1) % 3) + \
                abs((right - 1) // 3 - (e - 1) // 3)
            if ld > rd:
                right = e
                answer += 'R'
            elif ld < rd:
                left = e
                answer += 'L'
            else:
                if hand == 'right':
                    right = e
                    answer += 'R'
                else:
                    left = e
                    answer += 'L'

    return answer


numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"


solution(numbers, hand)
