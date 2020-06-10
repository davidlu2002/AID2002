"""
    multiprocessing模块创建进程
    １．编写进程函数
    ２．生产进程对象
    ３．启动进程
    ４．回收进程
"""
import multiprocessing as mp
from time import sleep

def fun01():
    print("开始进程１")
    sleep(3)
    print("子进程结束")

def fun02():
    print("开始进程２")
    sleep(5)
    print("父进程结束")

# 创建进程对象
p1 = mp.Process(target=fun01)


p1.start()  # 启动进程

# 父进程事件
fun02()

p1.join()   # 回收进程

# 等同于:
"""
pid = os.fork()
if pid == 0:
    fun01()
    os._exit()
else:
    fun02()
"""