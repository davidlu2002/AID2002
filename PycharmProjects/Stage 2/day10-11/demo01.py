"""
    创建套接字
"""
import socket

# 一、服务端只能连接一个客户端
"""
# 1 创建套接字
# family: AF_INET --> IPv4
# type： 套接字类型: SOCK_STREAM --> TCP | SOCK_DGRAM --> UDP
sockfd = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 2 绑定地址： ip+port
sockfd.bind(("127.0.0.1", 10025))

# 3 设置监听
sockfd.listen(5)
print("Waiting for connection...")

# 4 等待处理客户端的请求
connfd,addr = sockfd.accept()
print("Connected from {}".format(addr))

# 5 收发消息
while True:
    data = connfd.recv(1024)
    if data == b"":
        print("Connection has broken.")
        break
    print("Received message：",data.decode())
    n = connfd.send(b"Thanks for connection.")
    print("Sent {} bytes of message".format(n))

# 6 关闭套接字
connfd.close()
sockfd.close()
"""

# 二、服务端可以连接多个客户端
sockfd = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sockfd.bind(("127.0.0.1", 10025))
sockfd.listen(5)

while True:
    print("Waiting for connection...")

    connfd,addr = sockfd.accept()
    print("Connected from {}".format(addr))
    
    while True:
        data = connfd.recv(1024)
        if data == b"":
            print("Connection from {} has broken.".format(addr))
            break
        print("Received message：",data.decode())
        n = connfd.send(b"Thanks for connection.")
        print("Sent {} bytes of message".format(n))
    connfd.close()

sockfd.close()