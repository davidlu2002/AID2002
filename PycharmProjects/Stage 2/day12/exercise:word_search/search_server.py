dict_word = {"find":"找到", "clear":"清理","eliminate":"消灭"}

import socket
sockfd = socket.socket(type=socket.SOCK_DGRAM)
sockfd.bind(("127.0.0.1",10311))
print("Waiting for search...")

while True:
    result,addr = sockfd.recvfrom(1024)
    word_name = result.decode()
    search = False

    for key,value in dict_word.items():
        if word_name == key:
            sockfd.sendto(value.encode(),addr)
            search = True

    if not search:
        sockfd.sendto(b"No such word.", addr)




