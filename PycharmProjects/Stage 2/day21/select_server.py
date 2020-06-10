"""
    select_server.py IO多路复用　－－　select方法
"""

from socket import *
from select import select

# 创建监听套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',10311))
s.listen(3)

# 设置关注列表
rlist = [s] # s用于等待处理来自客户端的连接
wlist = xlist = []

# 循环监控IO
while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    # 遍历返回值列表，处理就绪的IO
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connected from",addr)
            rlist.append(c) #　增加新的IO监听
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            r.send(b'OK')

    for w in ws:
        pass

for x in xs:
    pass
