def sort(list):
    # 1번째 , 가운데, 마지막 원소 값의 크기를 정렬합니다.
    medianOfThree(list)

    # 길이가 3과 같거나 작은경우 위에서 정렬이 되었으므로 recursion이 종료됩니다.
    if len(list) <= 3:

        return list

    # 가운데 element를 pivot으로 설정합니다.
    pivot = list[len(list) // 2]

    # 뒤에서 두번째 idx와 mediaOfThree를 통해 구해낸 중간 pivot의 자리를 바꾸어줍니다.
    list[len(list) // 2], list[len(list) -
                               2] = list[len(list) - 2], list[len(list) // 2]

    # 바뀐 pivot을 이용하여 recursion을 진행합니다.
    # pivot보다 작은그룹, 같은그룹, 큰그룹으로 나눕니다.
    less = []
    eq = []
    more = []
    for k in list:
        if k < pivot:
            less.append(k)
        elif k > pivot:
            more.append(k)
        else:
            eq.append(k)
    # 각 그룹에서 따로 재귀를 호출하고 최종적으로 합쳐줍니다.
    return sort(less) + eq + sort(more)

    # pivot설정을 위해 1번째, 가운데, 마지막 원소의 값을 정렬하는 함수입니다.


def medianOfThree(list):
    # 길이가 1과 같거나 작은 경우 정렬이 필요없기 때문에 예외처리합니다.
    if len(list) <= 1:
        return

    # 1번째 , 가운데, 마지막 원소 값의 크기를 정렬합니다.
    if list[0] > list[len(list) // 2]:
        list[0], list[len(list) // 2] = list[len(list) // 2], list[0]
    if list[len(list) // 2] > list[len(list) - 1]:
        list[len(list) // 2], list[len(list) -
                                   1] = list[len(list) - 1], list[len(list) // 2]
    if list[0] > list[len(list) // 2]:
        list[0], list[len(list) // 2] = list[len(list) // 2], list[0]


# test코드입니다.
# print(sort([1, 2, 3, 4, -1, -2]))
