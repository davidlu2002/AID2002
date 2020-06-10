"""
    多进程
"""

import multiprocessing as mp
from time import sleep
import os

def fun01():
    sleep(2)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def fun02():
    sleep(3)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def fun03():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())

things = [fun01,fun02,fun03]
jobs = []

for th in things:
    p = mp.Process(target=th)
    jobs.append(p)
    p.start()

# 多个进程一起回收
for i in jobs:
    i.join()