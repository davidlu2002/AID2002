"""
    非阻塞IO
"""

from socket import *
from time import ctime,sleep

# 日志文件
f = open('log.txt','a+')

# TCP套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',10311))
sockfd.listen()

# 设置　套接字　为非阻塞
"""
sockfd.setblocking(False)
"""

# 设置　套接字　超时检测
sockfd.settimeout(3)

# 接受连接
while True:
    print("Waiting for connection...")
    # 没有客户端连接，每隔３秒写一条日志
    try:
        c,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        sleep(3)
        f.write("{} : {}\n".format(ctime(),e))
        f.flush()
    else:
        print("Connected from",addr)