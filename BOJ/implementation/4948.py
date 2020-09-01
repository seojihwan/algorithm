temp = [-1] * 250000


def isPrime(num):
    if not temp[num]:
        return False
    if temp[num] == 1:
        return True
    s = 2
    limit = int(pow(num, 0.5)) + 1
    while s < limit:
        if not (num % s):
            temp[num] = 0
            return False
        s += 1
    temp[num] = 1
    return True


while True:
    n = int(input())
    if not n:
        break
    cnt = 0
    for v in range(n + 1, 2*n + 1):
        if isPrime(v):
            cnt += 1
    print(cnt)
