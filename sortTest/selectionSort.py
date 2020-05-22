def sort(arr):
    # 순차적으로 배열의 0번째부터 최소값이 들어가도록 비교합니다.
    for i in range(len(arr)):
        temp = i
        for j in range(i + 1, len(arr)):
            if arr[temp] > arr[j]:
                temp = j

        # 자기 자신 보다 index가 큰것중 최소값을 갖는 index와 data를 바꿉니다.
        arr[i], arr[temp] = arr[temp], arr[i]
