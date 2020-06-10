import socket

# 1 创建套接字
socketfd = socket.socket(type=socket.SOCK_DGRAM)

# 2 绑定地址
socketfd.bind(("127.0.0.1",10311))

# 3 循环收发消息
while True:
    data,addr = socketfd.recvfrom(1024)
    print("Received:",data.decode())
    socketfd.sendto(b"Thanks",addr)

# 4 关闭套接字
socketfd.close()