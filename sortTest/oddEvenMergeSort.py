def merge(arr):
    temp = []
    # 데이터의 크기가 2가 될 때까지 분할하고, 좌우 값을 비교하여 바꾸어줍니다.
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
    i = 0
    mid = len(arr) // 2
    tmp = mid
    # 데이터를 합칠때, 홀짝 배열은 각각 정렬되있기 때문에 앞에서부터 크기를 비교하여
    # 배열에 추가하게되면, 정렬된 배열을 얻을 수 있습니다.

    # while문을 이용하여 홀 짝 배열을 각각 순차적으로 비교하여 배열에 추가하는데,
    # 한쪽의 배열이 다 입력이 끝나면, 자동으로 반대쪽 배열의 원소가 순차적으로 입력되도록 하였습니다.
    while i < 1 and mid < len(arr):
        if arr[i] > arr[mid]:
            temp.append(arr[mid])
            mid += 1
        else:
            temp.append(arr[i])
            i += 1
    for k in range(i, tmp):
        temp.append(arr[k])
    for k in range(mid, len(arr)):
        temp.append(arr[k])
    arr = temp
    return temp

    # 중간의 인덱스를 기준으로 분할하고, 분할한 배열을 merge함수에 입력해줍니다.


def oddEvenSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    first = oddEvenSort(arr[:mid])
    second = oddEvenSort(arr[mid:])
    temp = first + second
    return merge(temp)


def powerOfTwo(arr):
    n = 1
    # arr의 길이와, 변수 n을 이용하여 arr의 크기와 가까운 2의 거듭제곱을 찾습니다.
    while 2**n <= len(arr):
        # arr의 길이보다 큰 2의 거듭제곱중 가장 작은 n을 구합니다.

        n += 1
        # arr에 False를 추가하여 2의 거듭제곱 크기로 맞추어줍니다.
    for _ in range(2**n - len(arr)):
        arr.append(False)
    return arr

    # arr의 길이가 2의 거듭제곱이 아닌경우에 false를 추가해 주었기 때문에, 다시 false를 삭제해주는 과정입니다.


def removeFalse(arr):
    temp = []
    for element in arr:
        if element != False:
            temp.append(element)
    return temp

    # powerOfTwo함수는 arr의 크기가 2의 거듭제곱인지 확인
    # removeFalse를 통하여 정렬된 배열에서 본래의 크기로 수정해줍니다.


def sort(arr):
    arr = powerOfTwo(arr)
    arr = oddEvenSort(arr)
    arr = removeFalse(arr)
    return arr


# test코드입니다.
# data = [4, 3, 5, 6, 1, 7, 8, -1]
# data2 = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, -1]
# print(sort(data2))
