import socket
import struct

sockfd = socket.socket(type=socket.SOCK_DGRAM)
st = struct.Struct('i16sif')
addr = ("127.0.0.1",10311)
ID = 1

while True:
    name = input("Student name:")
    if name == "esc":
        sockfd.sendto(name.encode(),addr)
        break
    age = int(input("Student age:"))
    score = float(input("Student score:"))
    data = st.pack(ID,name.encode(),age,score)
    sockfd.sendto(data,addr)
    ID += 1

sockfd.close()
