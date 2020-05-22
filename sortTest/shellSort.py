
# 리스트와 gap을 인자로 받고 gap만큼 떨어진 element들을 삽입정렬합니다.


def insert(arr, gap):

    # gap만큼 떨어진 element들의 크기를 비교하여 순차적으로 삽입정렬합니다.
    for i in range(gap, len(arr)):
        temp = arr[i]
        j = i - gap
        # index 가 0보다 같거나 크고, 정렬이 필요한 경우만 대소비교를 하여 정렬합니다.
        while j >= 0 and arr[j] > temp:
            arr[j + gap] = arr[j]
            j -= gap
        arr[j + gap] = temp


def sort(arr):
    # 초기의 gap값은 arr의 크기 절반에서 시작합니다.
    d = len(arr) // 2
    # gap이 1일때 까지 gap을 반으로 줄이고 삽입정렬시킵니다.
    while d >= 1:
        insert(arr, d)
        d = d // 2
    return arr


# test코드입니다.
# print(sort([1, 2, 3, 4, -1, -2]))
