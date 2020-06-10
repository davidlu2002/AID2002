list01 = [1,3,4,12,11,55,13]
print(len(list01))
# 方法一：顺序排序
def fun01(list_target):
    for i in range(len(list_target)-1):
        for k in range(i, len(list_target)):
            if list_target[i] < list_target[k]:
                list_target[i],list_target[k] = list_target[k],list_target[i]

# 方法二：插入排序
def fun02(list_target):
    for i in range(1,len(list_target)):
        for k in range(i, 0, -1):
            if list_target[k] < list_target[k-1]:
                list_target[k], list_target[k-1] = list_target[k-1], list_target[k]
            else:
                break

# 方法三：冒泡排序
def fun03(list_target):
    for i in range(len(list_target)-1):
        for k in range(len(list_target)-1-i):
            if list_target[k] > list_target[k+1]:
                list_target[k],list_target[k+1] = list_target[k+1],list_target[k]

# 方法三：快速排序
def sub_sort(list_target,low,high):
    x = list_target[low]
    # low向后 high向左
    while low < high:
        # 后面的数往前放
        while list_target[high] >= x and high > low:
            high -= 1
        list_target[low] = list_target[high]
        while list_target[low] < x and low < high:
            low += 1
        list_target[high] = list_target[low]
    list_target[low] = x
    return low

def fun03_quick(list_target,low,high):
    if low < high:
        key = sub_sort(list_target,low,high)
        fun03_quick(list_target,low,key-1)
        fun03_quick(list_target,key+1,high)

# fun03_quick(list01,0,len(list01)-1)
# print(list01)
