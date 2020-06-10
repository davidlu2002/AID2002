import socket

socketfd = socket.socket()
socketfd.bind(("127.0.0.1",10311))
socketfd.listen(5)
print("Waiting for connection...")

connfd,addr = socketfd.accept()
print("Connected from {}".format(addr))

recv_file = open("recv_file.txt", "wb")

while True:
    data = connfd.recv(1024)
    if not data:
        break
    recv_file.write(data)

recv_file.close()
connfd.close()
socketfd.close()

