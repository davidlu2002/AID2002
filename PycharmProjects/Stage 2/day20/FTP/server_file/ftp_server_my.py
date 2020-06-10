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
class FTPServer:
    def __init__(self,c,addr):
        self.addr = addr
        self.c = c

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
            if file[0] != '.' and os.path.isfile(PATH + file):
                files += file + '\n'
        self.c.send(files.encode())

    def __download(self,name):
        name_ = PATH + name
        try:
            file = open(name_,mode="rb")
        except FileNotFoundError:
            self.c.send(b'No such file exists')
            return
        except Exception:
            self.c.send(b'An unexpected error occurs')
            return

        self.c.send(b'OK')

        while True:
            data = file.read(1024)
            if data == b'':
                sleep(0.1)
                self.c.send(b'complete')
                break
            self.c.send(data)
        print("{} successfully downloaded file '{}'".format(self.addr,name))

    def __upload(self,name):
        name_ = PATH + name
        if name in os.listdir(PATH):
            self.c.send(b'File already exists')
        else:
            self.c.send(b'OK')
        file = open(name_,mode="wb")
        while True:
            data = self.c.recv(1024)
            if data == b'complete':
                print("{} successfully uploaded file '{}'".format(self.addr,name))
                break
            file.write(data)

    def run(self):
        while True:
            data = self.c.recv(1024)
            msg = data.decode().split(" ",1)

            if not data or msg[0] == "Q":
                print("{} has logged out".format(self.addr))
                return
            if msg[0] == "L":
                self.__list()
            elif msg[0] == "D":
                self.__download(msg[1])
            elif msg[0] == "U":
                self.__upload(msg[1])

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

        server = FTPServer(c,addr)
        t = Thread(target=server.run)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()