
def partition(list, left, right):
    pivot = list[right]
    low = left
    print('right',right)
    high = right - 1
    while low <= high:
        while list[low] < pivot and low <= right:
            low += 1
        while list[high] > pivot and high >= left:
            high -= 1
            print('high2',high)
        if low <= high:
            print('low',low,'high',high)
            list[low], list[high] = list[high], list[low]
            low, high = low + 1, high - 1
    print('low',low,'high',high)
    list[low], list[right] = list[right], list[low]
    return low
def quick_sort(list, left, right):
    if(left < right):
        pos = partition(list, left, right)
        print('pos', pos)
        print(list)

        quick_sort(list, left, pos-1)
        quick_sort(list, pos+1, right)
        

list = [5, 3, 1, 8, 11, 4 ,7 ]
quick_sort(list, 0, 6)
print(list)



