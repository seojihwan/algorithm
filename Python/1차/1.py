import re


def solution(new_id):
    n = new_id.lower()
    n = ''.join(re.findall("[a-z]|[0-9]|-|_|[.]", n))
    for _ in range(len(n)):
        n = n.replace('..', '.')
    if len(n) and n[0] == '.':
        n = list(n)
        n[0] = ''
        n = ''.join(n)
    if len(n) and n[-1] == '.':
        n = list(n)
        n[-1] = ''
        n = ''.join(n)
    if not len(n):
        n = 'a'
    if len(n) >= 16:
        n = n[:15]
        if n[-1] == '.':
            n = list(n)
            n[-1] = ''
            n = ''.join(n)
    if len(n) <= 2:
        while len(n) < 3:
            n += n[-1]
    answer = n
    return answer


s = ["...!@BaT#*..y.abcdefghijklm"	, "z-+.^.",
     "=.=", "123_.def", "abcdefghijklmn.p"]
for i in range(4):
    print(solution(s[i]))
