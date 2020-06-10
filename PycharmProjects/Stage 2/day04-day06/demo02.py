# 二分查找


# 方法一
'''
def fun02(list_target, item):
    """
        输入元素数值，返回列表内是否有该元素
    :param list_target: 升序排列的列表
    :param item: 数值
    :return: True: 含有   False：不含有
    """
    n = len(list_target)
    if n == 0:
        return None

    if n % 2 != 0:
        if n == 1:
            return item == list_target[0]
        n = n+1
        m = int(n/2)
        if item == list_target[m]:
            return True
        elif item > list_target[m]:
            if fun02(list_target[m::],item):
                return True
            return False
        else:
            if fun02(list_target[:m:],item):
                return True
            return False

    if n % 2 == 0:
        m1 = int(n/2)
        m2 = int((n+2)/2)
        if n == 2 and item != list_target[0] and item  != list_target[1]:
            return False
        if item == list_target[m1] or item  == list_target[m2]:
            return True
        elif item > list_target[m2]:
            if fun02(list_target[m2::],item):
                return True
            return False
        elif item < list_target[m1]:
            if fun02(list_target[:m1:],item):
                return True
            return False
'''

# 方法二

def search01(list_target, key):
    low,high = 0,len(list_target)-1
    while low <= high:
        mid = (low + high) // 2
        if list_target[mid] < key:
            low = mid + 1
        elif list_target[mid] > key:
            high = mid - 1
        else:
            return mid


"""
def fun01(list_target, item):
    n = len(list_target)
    if n > 0:
        mid = n // 2
        if list_target[mid] == item:
            return True
        elif list_target[mid] < item:
            return fun01(list_target[mid+1::],item)
        else:
            return fun01(list_target[:mid:],item)
    return False
"""

list01 = []
for i in range(30):
    list01.append(i)

print(search01(list01,29))