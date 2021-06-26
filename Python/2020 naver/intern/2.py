def solution(N):
    strN = str(N)
    isPlus = True
    if strN[0] == '-':
        strN = strN[1:]
        isPlus = False
    length = len(strN)
    if isPlus:
        answer = -8000
        for i in range(length + 1):
            answer = max(answer, int(strN[:i] + '5' + strN[i:]))
        return str(answer)
    else:
        answer = 8000
        for i in range(length + 1):
            answer = min(answer, int(strN[:i] + '5' + strN[i:]))
        return '-' + str(answer)


N = 268
print(solution(N))
