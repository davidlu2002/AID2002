"""
    thread_lock.py  线程锁演示
"""

from threading import Thread,Lock

a = b = 0
lock = Lock()

def value():
    while True:
        if a != b:
            lock.acquire()
            print("a =",a)
            print("b =",b)
            lock.release()

t = Thread(target=value)
t.start()

while True:
    lock.acquire()
    a += 1
    b += 1

