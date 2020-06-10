"""
    传参的多进程
"""
from multiprocessing import Process
from time import sleep

def fun01(a,b):
    sleep(2)
    print("%d + %d = %d" % (a,b,a+b))

def fun02(c=0,d=0):
    sleep(2.5)
    print("%d - %d = %d" % (c,d,c-d))

p1 = Process(target=fun01,args=(1,2))
p2 = Process(target=fun02,kwargs={"c":4,"d":2})
p1.start()
p2.start()

p1.join()
p2.join()
