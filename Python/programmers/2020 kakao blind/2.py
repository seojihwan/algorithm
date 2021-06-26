def solution(p):
    answer = ''
    if not len(p):
        return answer

    def swap(pp):
        temp = ''
        for e in pp:
            if e == '(':
                temp += ')'
            else:
                temp += '('
        return temp

    def b(pp):
        if pp == '':
            return solution(pp)
        lc, rc = 0, 0
        u, v = '', ''
        for idx, e in enumerate(pp):
            if e == "(":
                lc += 1
            elif e == ")":
                rc += 1
            if lc and rc and lc == rc:
                print(pp[:idx + 1])
                u = pp[:idx + 1]
                v = (pp[idx + 1:])
                break
        if u[-1] == ')':
            return u + solution(v)
        else:
            return '(' + solution(v) + ')' + swap(u[1:-1])
    answer = b(p)
    return answer


for e in ["(()())()", ")(", "()))((()"]:
    print(solution(e))
