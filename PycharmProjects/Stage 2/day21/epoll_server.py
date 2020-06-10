"""
    epoll_server.py  epoll方法的IO多路复用
"""

from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 10311))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，可以通过一个IO的fileno找到IO对象
fdmap = {s.fileno(): s}

# 关注s
ep.register(s, EPOLLIN|EPOLLERR)

# 循环监控IO发生
while True:
    events = ep.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connected from", addr)
            ep.register(c, EPOLLIN|EPOLLERR)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:  # 判断是否为POLLIN就绪
            data = fdmap[fd].recv(1024)
            if not data:
                del fdmap[fd]
                ep.unregister(fd)  # 取消关注

                continue
            print(data.decode())
            fdmap[fd].send(b'OK')