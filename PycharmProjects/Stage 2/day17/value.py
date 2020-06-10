"""
    value.py
    共享内存
    注意：此共享内存当中只能有一个值
"""

from multiprocessing import Value,Process
import time,random

# 创建共享内存
money = Value('i',5000)

# 操作共享内存
def man():
    for i in range(30):
        time.sleep(0.1)
        money.value += random.randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.1)
        money.value -= random.randint(100,800)

p1 = Process(target=man)
p2 = Process(target=girl)

p1.start()
p2.start()

p1.join()
p2.join()

# 获取共享内存
print("一个月余额：",money.value)
