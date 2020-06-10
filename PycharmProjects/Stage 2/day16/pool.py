"""
    进程池范例
"""
from multiprocessing import Pool
from time import *

def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

# 创建进程池
pool = Pool()

#　向进程池队列添加进程
for i in range(10):
    msg = "Tarena %d" % (i)
    pool.apply_async(func=worker,args=(msg,))

# 关闭进程池
pool.close()

# 结束进程池内的进程
pool.join()