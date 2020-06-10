"""
    创建客户端
"""

import socket

# 1 创建套接字
socketfd = socket.socket()

# 2 建立连接
socketfd.connect(("0.0.0.0", 10025))

# 3 收发消息(必须为字节串)
while True:
    data = input("data>>>")
    if "esc" == data:
        break
    socketfd.send(data.encode())
    rev_data = socketfd.recv(1024)
    print("Have received message：", rev_data.decode())

# 4 关闭套接字
socketfd.close()