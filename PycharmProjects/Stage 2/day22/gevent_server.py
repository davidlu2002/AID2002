"""
    gevent_server.py    基于协程的TCP并发
"""

import gevent
from gevent import monkey
monkey.patch_all()  # 执行脚本，修改所有的阻塞

from socket import *

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')

s = socket()
s.bind(('0.0.0.0',10311))
s.listen(3)

while True:
    c,addr = s.accept()
    print("Connected from",addr)
    # handle(c)   # 处理客户端收发消息
    gevent.spawn(handle,c)