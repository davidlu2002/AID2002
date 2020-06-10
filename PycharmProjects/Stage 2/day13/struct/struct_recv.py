import struct
import socket
s = open("student_info.txt", "a")

sockfd = socket.socket(type=socket.SOCK_DGRAM)
st = struct.Struct('i16sif')
sockfd.bind(("127.0.0.1",10311))

while True:
    print("Waiting for recording...")
    data,addr = sockfd.recvfrom(1024)
    if data == b"esc":
        print("Recording ends.")
        break
    info = st.unpack(data)
    name_ = info[1].decode()
    name = name_.replace(b"\x00".decode(),"")
    s.write("{} {}-age:{} score:{}\n".format(info[0],name,info[2],round(info[3])))
    s.flush()
    print("Successfully recorded")

sockfd.close()
s.close()

