"""
    广播接受
    １．创建ｕｄｐ套接字
    ２．设置套接字可以发送接受广播
    ３．选择端口
    ４．接收广播
"""

import socket
s = socket.socket(type=socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.bind(("0.0.0.0",10311))

while True:
    msg,addr = s.recvfrom(1024)
    print("Received:",msg.decode())