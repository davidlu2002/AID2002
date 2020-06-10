"""
    ftp_server.py 文件服务器，服务端
"""

from socket import *
from threading import Thread
from time import sleep
import os
import sys

# 全局变量
ADDR = ('0.0.0.0',10311)
PATH = "/home/tarena/PycharmProjects/FTP/"

# 创建类，实现服务器文件处理功能
class FTPServer(Thread):
    def __init__(self,c,addr):
        self.addr = addr
        self.c = c
        super().__init__()

    def __list(self):
        file_list = os.listdir(PATH)
        if not file_list:
            self.c.send("No file exists")
            return
        else:
            self.c.send(b'OK')
            sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(PATH+file):
                files += file + '\n'
        self.c.send(files.encode())


    def __download(self,name):
        if name not in file_list or name == "esc":
            self.c.send("None")
            return
        file = open(name,mode="rb")
        while True:
            data = file.read(1024)
            self.c.send(data)
            print(data)
            if not data:
                break
        print("{} successfully downloaded file '{}'".format(self.addr,name))

    def __upload(self):
        pass

    def run(self):
        while True:
            data = self.c.recv(1024)
            msg = data.decode().split(" ",1)
            if not msg or msg[0] == "Q":
                print("{} has logged out".format(self.addr))
                return
            elif msg[0] == "L":
                self.__list()
            elif msg[0] == "D":
                self.__download(msg[1])
            elif msg[0] == "U":
                self.__upload()

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    print("PORT 10311 waiting for connection...")
    while True:
        try:
            c, addr = s.accept()
            print("Connected from",addr)
        except KeyboardInterrupt:
            sys.exit("Server shut down")
        except Exception as e:
            print(e)
            continue

        client = FTPServer(c,addr)
        client.setDaemon(True)
        client.start()

if __name__ == '__main__':
    main()