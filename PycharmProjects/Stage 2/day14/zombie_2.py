"""
    创建二级子进程，处理僵尸进程
"""

import os
from time import sleep

def fun01():
    for i in range(3):
        sleep(2)
        print("写代码")

def fun02():
    for i in range(2):
        sleep(4)
        print("测代码")

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:  # 一级子进程
    pid_ = os.fork()
    if pid_ == 0:   # 二级子进程
        fun01()
    else:
        os._exit(0)
else:
    os.wait() # 等一级子进程退出
    fun02()
