n = int(input())


def isPrime(num):
    if num == 2:
        return True
    if num == 1 or not (num % 2):
        return False
    t = 3
    size = int(pow(num, 0.5)) + 1
    while t < size:
        if not num % t:
            return False
        t += 2
    return True


num = 0


def dfs(idx):
    global num
    if idx == n:
        print(num)
        return
    for e in range(1, 10):
        num = num * 10 + e
        if isPrime(num):
            dfs(idx + 1)
        num = (num - e) // 10


dfs(0)
