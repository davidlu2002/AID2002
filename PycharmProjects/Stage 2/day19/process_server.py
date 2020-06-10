"""
    process_server.py   基于Process的多进程并发
"""

from socket import *
from multiprocessing import Process
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 10311
ADDR = (HOST,PORT)

# 具体处理客户端请求
def handle(c,addr):
    while True:
        data = c.recv(1024)
        if not data:
            print("Connection from {} has broken.".format(addr))
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    print("PORT 10311 waiting for connection...")
    os._exit(0)

# 创建TCP套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("PORT 10311 waiting for connection...")

while True:
    try:
        c,addr = s.accept()
        print("Connected from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端
    p = Process(target=handle,args=(c,addr))
    p.daemon = True # 父进程结束则所有进程结束
    p.start()
    c.close()