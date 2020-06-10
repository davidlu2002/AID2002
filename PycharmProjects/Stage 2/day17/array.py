"""
array.py
共享内存，存放一组数据
"""

from multiprocessing import Process,Array

"""
# 创建共享内存
# shm = Array('i',[1,2,3,4])
shm = Array('i',5)  # 初始开辟５个整形的列表

def fun():
    # array创建的共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = 1000

p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)
"""

# 创建共享内存
shm = Array('c',b'Hello')

def fun():
    # array创建的共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = b'B'

p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)

print(shm.value)    # 打印整个字节串