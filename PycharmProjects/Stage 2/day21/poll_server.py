"""
    poll_server.py poll方法的IO多路复用
"""

from socket import *
from select import *

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',10311))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典，可以通过一个IO的fileno找到IO对象
fdmap = {s.fileno():s}

# 关注s
p.register(s,POLLIN|POLLERR)

# 循环监控IO发生
while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connected from",addr)
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()] = c
        elif event & POLLIN:  # 判断是否为POLLIN就绪
            data = fdmap[fd].recv(1024)
            if not data:
                del fdmap[fd]
                p.unregister(fd) # 取消关注

                continue
            print(data.decode())
            fdmap[fd].send(b'OK')