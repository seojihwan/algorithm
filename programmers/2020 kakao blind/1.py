def solution(s):
    answer = 1000
    for x in range(1, len(s) + 1):
        c = 0
        temp = ""
        cnt = 1
        while c + x <= len(s) + 1:
            if s[c:c + x] == s[c + x: c + 2*x]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + s[c:c + x]
                else:
                    temp += s[c:c + x]
                cnt = 1
            c += x
        temp += s[c:]
        answer = min(answer, len(temp))

    return answer
