def addTime(a, b, c):
    ma, da = map(int, a.split('/'))
    hb, mb, sb = map(int, b.split(':'))
    c = int(c)

    mb += c
    if mb >= 60:
        mb -= 60
        hb += 1

    if hb >= 24:
        hb -= 24
        da += 1

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if da > days[ma]:
        da -= days[ma]
        ma += 1

    # print(ma, da, hb, mb, sb)

    return str(ma) + '/' + str(da) + ' ' + str(hb) + ':' + str(mb) + ':' + str(sb)


def findmin(ta, tb, ka, kb, ti, idx):

    aa, bb = map(int, ta.split('/'))
    cc, dd = map(int, ka.split('/'))

    ee, ff, gg = map(int, tb.split(':'))
    hh, jj, ii = map(int, kb.split(':'))

    if aa > cc:
        return ka, kb, idx
    elif aa < cc:
        return ta, tb, ti

    if bb > dd:
        return ka, kb, idx
    if bb < dd:
        return ta, tb, ti

    if ee > hh:
        return ka, kb, idx
    if ee < hh:
        return ta, tb, ti

    if ff > jj:
        return ka, kb, idx
    if ff < jj:
        return ta, tb, ti

    if gg > ii:
        return ka, kb, idx
    if gg < ii:
        return ta, tb, ti

    return ka, kb, idx


def solution(n, customers):
    keys = ['' for _ in range(n)]
    # print(keys)
    cnt = [0 for _ in range(n)]
    for customer in customers:
        a, b, c = customer.split(' ')
        # print(a, b, c)
        addTime(a, b, c)

        ta, tb = '20/31', '25:25:25'
        ti = 10000000
        for idx, key in enumerate(keys):
            print(idx, keys, "kkkkkkkkkkkkkkkkkkkkkkkkkk")
            if key == '':
                cnt[idx] += 1
                keys[idx] = addTime(a, b, c)
                break
            # print(key, 'key')
            ka, kb = key.split(' ')
            print(ta, tb, ka, kb, idx, ti, "비교시작")
            ta, tb, ti = findmin(ta, tb, ka, kb, ti, idx)
            print(ta, tb, ka, kb, idx, ti, "비교 끝")
            if idx == len(keys) - 1:
                print(ti)
                cnt[ti] += 1
                print(ta, tb,  "??????????")
                keys[ti] = addTime(ta, tb, c)
    print(cnt)
    answer = 0
    for e in cnt:
        answer = max(answer, e)
    return answer


n = 2
c = ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 01"]
print(solution(n, c))
