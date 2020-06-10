"""
    event 线程互斥方法演示
"""

from threading import Thread,Event

s = None
e = Event()


def fun01():
    print("程序1请求登录")
    global s
    s = "天王盖地虎"
    e.set() # 操作完共享资源(s),设置e

t = Thread(target=fun01)
t.start()

print("确认用户名和密码")
e.wait()    #　人为设置阻塞，直至e.set()执行后
if s == "天王盖地虎":
    print("登录成功")
else:
    print("登录失败")

t.join()