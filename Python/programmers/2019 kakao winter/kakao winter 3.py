def solution(user_id, banned_id):
    answer = 0
    temp = [[] for _ in banned_id]

    def isSame(a, b):
        if len(a) == len(b):
            for n in range(len(a)):
                if b[n] == "*":
                    continue
                elif (a[n] != b[n]):
                    return False
            return True
        else:
            return False

    for u in range(len(user_id)):
        for b in range(len(banned_id)):
            if isSame(user_id[u], banned_id[b]):
                temp[b].append(u)

    temp2 = []

    def bp(tmp, x):
        if x == len(temp):
            if tmp not in temp2:
                return temp2.append(tmp)
        else:
            for y in range(len(temp[x])):
                if temp[x][y] not in tmp:
                    tmp.append(temp[x][y])
                    bp(sorted(tmp), x + 1)
                    tmp.pop()
    bp([], 0)

    answer = len(temp2)
    return answer


