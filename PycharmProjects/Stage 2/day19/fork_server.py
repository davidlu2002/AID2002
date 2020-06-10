"""
    fork_server.py 基于fork的多进程并发
步骤：
    １．创建TCP套接字（UDP用法灵活，不太需要多进程并发）
    ２．等待接受客户端请求
    ３．客户端连接，创建新的进程处理客户端请求
    ４．原进程继续等待其他客户端连接
    ５．客户端退出，销毁创建的进程
"""

from socket import *
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
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c,addr)
        os._exit(0)
    else:
        c.close()


