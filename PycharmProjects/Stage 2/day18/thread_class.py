"""
    自定义线程类
"""

from threading import Thread

# 自定义线程类
class ThreadClass(Thread):
    def __init__(self,*args,**kwargs):
        self.attr = args[0]
        super().__init__()

    def f1(self):
        print("step 1")
    def f2(self):
        print("step 2")
    # 重写run 逻辑调用
    def run(self):
        self.f1()
        self.f2()

t = ThreadClass('abc')
t.start()   # 运行start时，自动运行run方法
t.join()