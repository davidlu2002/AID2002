def quick_sort(alist):
    if len(alist) < 2:
        return alist
    first = alist[0]
    alist.remove(first)

    left,right = [],[]
    for i in alist:
        if i > first:
            right.append(i)
        else:
            left.append(i)
    res = quick_sort(left) + [first] + quick_sort(right)
    return res


l1 = [6,3,2,6,8,1,2,0,123]
print(quick_sort(l1))