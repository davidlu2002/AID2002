from socket import *
from threading import Thread
import os

s = socket()
s.bind(('0.0.0.0',10312))
s.listen(3)

class Fun():
    def fun01(self):
        print("=================")

while True:
    print("waiting for connection")
    try:
        c,addr = s.accept()
        print("Connected from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    f = Fun()
    t = Thread(target=f.fun01)
    t.start()
