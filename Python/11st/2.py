# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    n = len(S)
    m = len(S[0])
    answer = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if S[i][k] == S[j][k]:
                    answer.append(i)
                    answer.append(j)
                    answer.append(k)
                    return answer
    return []


s = []
solution(s)
