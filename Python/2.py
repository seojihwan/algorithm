from itertools import combinations


def solution(table):
    n = len(table[0])
    m = len(table)
    orderList = [i for i in range(n)]
    for i in range(1, n + 1):
        orderCombList = tuple(combinations(orderList, m))
        for comb in orderCombList:
            temp = [0 for _ in range(n)]
            print(temp, "start")
            for el in comb:
                for elementIdx, element in enumerate(table[el]):
                    if element == 'O':
                        temp[elementIdx] = 1
                    print(temp, "end")
                    if 0 not in temp:
                        print(i)
                        return i


# solution(["XOXO", "OXXO", "XXOX", "XOOO"])
solution(["OXXO", "XOXO", "XXOO"])
# solution(["OXOXO", "OOOOO", "XOXOX"])
