def lowerBound(list, n, key):   #binary search
    s = 0
    e = n-1
    while e - s > 1:
        mid = (s+e) // 2
        if list[mid] < key:
            s = mid        
        elif list[mid] > key:
            e = mid
        else:
            return mid
    if list[s] < key :
        return e
    else :
        return s