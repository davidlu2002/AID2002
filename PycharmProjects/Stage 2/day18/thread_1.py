"""
    thread_1.py 线程使用1
"""

from threading import Thread
from time import sleep
import os

a = 1   #　主线程的变量

def fun():
    for i in range(3):
        print(os.getpid(),"运行程序1")
        sleep(2)
        print("程序1运行完毕")
    global a
    print("a =",a)
    a = 10000   #　分支线程内改变主线程的变量

# 创建线程对象
t = Thread(target=fun)
t.start()   # 启动线程

# 主线程代码与分支线程代码同时执行
for i in range(4):
    print(os.getpid(),"运行程序2")
    sleep(1)
    print("程序2运行完毕")

t.join()    # 回收线程
print("main a:",a)  # 所有线程共用一块空间