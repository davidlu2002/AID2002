"""
    thread_2    线程函数参数演示
"""

from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    sleep(sec)
    print("{}用{}秒执行完毕".format(name,sec))

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={'name':'T{}'.format(i)})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()