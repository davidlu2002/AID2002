import socket
sockfd = socket.socket(type=socket.SOCK_DGRAM)
addr = ("127.0.0.1",10311)

while True:
    data = input("Word:")
    if data == "":
        break
    sockfd.sendto(data.encode(),addr)
    result, addr = sockfd.recvfrom(1024)
    print(result.decode())

sockfd.close()
