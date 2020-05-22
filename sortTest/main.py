import time  # 시간 측정을 위한 time library
import selectionSort
import medianOfThreeQuickSort
import shellSort
import bitonicSort
import oddEvenMergeSort


name = "12141718 서지환 "
sort_name = "oddEvenMergeSort "
# 먼저 txt파일을 열고, 리스트에 저장하고, 임포트한 각 정렬의 sort함수를 호출하여
# 데이터를 정렬합니다.
# 그 후 시작시간과 정렬된 후의 시간의 차를 이용하여
# ms단위의 측정시간을 log로 보여줍니다.
with open('./10000.txt', 'r') as file:    # data 10000
    n = file.readline()
    temp = file.readline()
    arr = list(map(int, temp.split()))
start = time.time()
oddEvenMergeSort.sort(arr)  # 해당 모듈 대신 다른 모듈의 이름을 넣으면 정렬 알고리즘을 바꿀 수 있습니다.
title = name + sort_name + "data size: 10000"

# ms 단위로 처리시간을 보여줍니다.
print(title, "실행시간: ", round((time.time() - start) * 1000), "ms")

with open('./50000.txt', 'r') as file:    # data 50000
    n = file.readline()
    temp = file.readline()
    arr = list(map(int, temp.split()))
start = time.time()
oddEvenMergeSort.sort(arr)
title = name + sort_name + "data size: 50000"
print(title, "실행시간: ", round((time.time() - start) * 1000), "ms")

with open('./100000.txt', 'r') as file:    # data 100000
    n = file.readline()
    temp = file.readline()
    arr = list(map(int, temp.split()))
start = time.time()
oddEvenMergeSort.sort(arr)
title = name + sort_name + "data size: 100000"

print(title, "실행시간: ", round((time.time() - start) * 1000), "ms")

with open('./500000.txt', 'r') as file:    # data 500000
    n = file.readline()
    temp = file.readline()
    arr = list(map(int, temp.split()))
start = time.time()
oddEvenMergeSort.sort(arr)
title = name + sort_name + "data size: 500000"

print(title, "실행시간: ", round((time.time() - start) * 1000), "ms")

with open('./1000000.txt', 'r') as file:    # data 1000000
    n = file.readline()
    temp = file.readline()
    arr = list(map(int, temp.split()))
start = time.time()
oddEvenMergeSort.sort(arr)
title = name + sort_name + "data size: 1000000"

print(title, "실행시간: ", round((time.time() - start) * 1000), "ms")
