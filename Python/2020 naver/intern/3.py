# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, C):
    length = len(S)
    s, e = 0, 1
    answer = 0
    while s < length and e < length:
        if S[s] == S[e]:
            if C[s] > C[e]:
                answer += C[e]
                C[e] = C[s]
            else:
                answer += C[s]
        s = e
        e += 1

    return answer


s = "baaab"
c = [333, 111,222,111,111]
print(solution(s, c))
