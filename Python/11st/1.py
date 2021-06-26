
def solution(S):
    if 'aaa' in S:
        return -1

    a_count = S.count('a')

    # write your code in Python 3.6
    return 2 * (len(S) - a_count + 1) - a_count


s = "z"
print(solution(s))
