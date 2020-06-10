"""
sem.py  进程间通信：信号量
"""

from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量(最多允许3个任务同时执行)
sem = Semaphore(3)

# 任务函数
def task():
    sem.acquire()   # 执行任务必须消耗一个信号量
    print("{}执行任务".format(os.getpid()))
    sleep(2)
    print("{}执行任务完毕".format(os.getpid()))
    sem.release()   #　归还信号量

for i in range(10):
    p = Process(target=task)
    p.start()
