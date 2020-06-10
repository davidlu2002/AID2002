import socket

# 1 创建套接字
sockfd = socket.socket(type=socket.SOCK_DGRAM)

# 2 循环收发消息
addr = ("127.0.0.1",10311)

while True:
    data = input("data>>>")
    if data == "esc":
        break
    sockfd.sendto(data.encode(),addr)
    recv_msg,addr = sockfd.recvfrom(1024)
    print(addr)
    print("Received:", recv_msg.decode())
sockfd.close()
