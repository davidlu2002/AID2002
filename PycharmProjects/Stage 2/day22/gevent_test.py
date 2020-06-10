import gevent

def fun01(a,b):
    print("Running fun01...",a,b)
    gevent.sleep(2)
    print("Running fun01 completed")

def fun02():
    print("Running fun02...")
    gevent.sleep(3)
    print("Running fun02 complete")
f = gevent.spawn(fun01,1,2)
b = gevent.spawn(fun02)

gevent.joinall([f,b])
