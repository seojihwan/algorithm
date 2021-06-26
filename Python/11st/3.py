# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A = sorted(A)
    n = len(A)
    answer = 0
    for i in range(n):
        if (i + 1) != A[i]:
            answer += abs(i + 1 - A[i])
            if answer >= 1000000000:
                return -1
    # write your code in Python 3.6
    return answer


a = [6, 2, 3, 5, 6, 3]
a = [200000] * 200000
print(solution(a))
