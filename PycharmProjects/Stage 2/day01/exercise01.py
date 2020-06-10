# 通过计算列表运行append/insert方法，证明列表的数据结构是线性的顺序存储结构

import time

def get_action_time(list_target, func):
    start_time = time.time()
    func(list_target)
    end_time = time.time()
    return end_time - start_time

def compare_insert_append(element_amount):
    list01 = []
    if element_amount > 10000000 or element_amount < 0:
        raise ValueError("无法计算（数量过大或有误）")

    for item in range(element_amount):
        list01.append(item)
    time01 = get_action_time(list01, lambda item: item.append(100))

    list01.pop(len(list01) - 1)
    time02 = get_action_time(list01, lambda item: item.insert(2, 100))
    print("数据量为{}时，insert方法运行时间是append方法运行时间的{}倍".format(element_amount,round(time02 / time01, ndigits=3)))

# 1 数据量较小时
compare_insert_append(10)
compare_insert_append(1000)
# 2 数据量为中等数量
compare_insert_append(10000)
# 3 数据量较大时
compare_insert_append(1000000)

# 可以看到，随着数据量的增加，insert方法运行时间与append方法运行时间的比值迅速增加。