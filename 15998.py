n = int(input())

log = []
for k in range(n):
    log.append(list(map(int, input().split())))


def divisor(n, low, high):
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            if low < i and i <= high:
                div.append(i)
            # 약수임
    return div


turn = False
error = False
div = []
for m in range(n):
    if log[m][0] < 0:
        # 소비
        if (m - 1 >= 0):
            if log[m-1][1] < abs(log[m][0]):
                turn = True
                charge = log[m][1] + abs(log[m][0]) - log[m-1][1]
                div.append(divisor(charge, log[m][1], charge))
                # div = list(filter(lambda x: (x > min), div))
                # print(div)
            else:
                if log[m-1][1] - abs(log[m][0]) != log[m][1]:
                    error = True
        else:
            charge = log[m][1] + abs(log[m][0])
            div.append(divisor(charge, log[m][1], charge))
sol = []
max = 100000000000
min = -1
for k in range(len(div)):
    if (max > div[k][len(div[k]) - 1]):
        max = div[k][len(div[k]) - 1]
    if (min < div[k][0]):
        min = div[k][0]
        if (max < min):
            min = 100000000000

    # div[k] = list(filter(lambda x:)
for k in range(len(div)):
    sol.append(list(filter(lambda x: (x >= min and x <= max), div[k])))
    if len(sol[k]) >= 1 and error == False:
        print(sol[k][0])
        break
    elif (k == len(div) - 1 and error == False):
        print(-1)
if (turn == False and error == False):
    print(1)
if (error == True):
    print(-1)
# print(sol)
# if(len(sol) >= 1):
#     print(sol[0])
# else:
#     print(-1)
