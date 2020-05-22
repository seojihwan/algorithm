
# arr와 bool type 변수를 매개변수로 갖는 bitonicSort함수입니다.


def bitonicSort(arr, isUp=True):
    # 길이가 1이하이면 return됩니다.
    if len(arr) <= 1:
        return arr
    # 가운데 index를 기준으로 2개의 배열로 나누어 bitonicSort를 재귀호출합니다.
    mid = len(arr) // 2

    # mid를 중심으로 앞의 절반은 뒤의 절반보다 항상 크게됩니다.
    first = bitonicSort(arr[:mid], True)
    second = bitonicSort(arr[mid:], False)

    # 나뉘어진 2배열을 합해주는 merge함수를 return합니다.
    return merge(first + second, isUp)


# arr와 bool type 변수를 매개변수로 갖는 merge함수입니다.


def merge(arr, isUp):
    # 길이가 1이하이면 return됩니다.
    if len(arr) == 1:
        return arr

    # merge함수의 bool type 매개변수 isUp에 따라, 오름차순 내림차순으로 원소들을 swap합니다.
    swap(arr, isUp)

    mid = len(arr) // 2
    # 분할된 배열을 다시 mid를 중심으로 2분할 하여 swap해주는 과정을 재귀호출합니다.
    first = merge(arr[:mid], isUp)
    second = merge(arr[mid:], isUp)
    # 분할된 배열을 합쳐서 return합니다.
    return first + second


def swap(arr, isUp):
    # merge함수의 bool type 매개변수 isUp에 따라, 오름차순 내림차순으로 원소들을 swap합니다.

    mid = len(arr) // 2
    # mid를 중심으로 오름차순, 내림차순이 다르기 때문에 isUp에 따라 데이터를 정렬합니다.

    for i in range(mid):
        if (arr[i] > arr[mid + i]) == isUp:
            arr[i], arr[mid + i] = arr[mid + i], arr[i]

    # bitonicSort의 경우 원소의 갯수가 2의 거듭제곱이어야 하기 때문에 check함수를 만들었습니다.


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
    # bitonicSort를 통한 정렬
    # removeFalse를 통하여 정렬된 배열에서 본래의 크기로 수정해줍니다.


def sort(arr):
    arr = powerOfTwo(arr)
    arr = bitonicSort(arr)
    arr = removeFalse(arr)
    return arr


# test코드입니다.
# print(sort([1, 2, 3, 4, -1, -2]))
