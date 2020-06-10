from socket import *

ADDR = ('127.0.0.1',10311)
s = socket()
s.connect(ADDR)

while True:
    data = input(">>>")
    if data == "":
        break
    s.send(data.encode())
    msg = s.recv(1024)
    print("Recevied from server:",msg.decode())

s.close()
