def quick_sort(list):
    if len(list) <=1 :
        return list
    pivot = list[len(list)//2][0]
    
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
    return quick_sort(less) + eq + quick_sort(more)