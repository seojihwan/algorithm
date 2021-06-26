import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())


def solution(m, k):
    answer = ''
    lm, lk = len(m), len(k)
    sm, sk = 0, 0
    while sm < lm:
        if sk < lk and m[sm] == k[sk]:
            sk += 1
        else:
            answer += m[sm]
        sm += 1
    return answer


m = ["kkaxbycyz", "acbbcdc"]
k = ["abc", "abc"]
for i in range(2):
    print(solution(m[i], k[i]))
