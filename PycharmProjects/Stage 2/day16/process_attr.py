"""
    进程对象属性
"""

from multiprocessing import Process
import time

def tm():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())

p = Process(target=tm)
p.daemon = True # 父进程结束，子进程也结束

p.start()

p.name = "ABC"
print("Name:",p.name)   # 进程名称
print("PID:",p.pid)     # 对应子进程的ＰＩＤ号
print("is alive:",p.is_alive()) # 对应子进程是否在生命周期内

