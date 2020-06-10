import socket

socketfd = socket.socket()
socketfd.connect(("127.0.0.1",10311))
filename = input("Filename:")
file = open(filename, "rb")

while True:
    data = file.read(1024)
    if not data:
        break
    socketfd.send(data)


file.close()
socketfd.close()
