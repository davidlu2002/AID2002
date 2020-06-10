"""
    ftp_client.py 文件服务，客户端
"""

from socket import *
import sys

# 全局变量
ADDR = ('0.0.0.0',10311)

# 客户端文件处理类
class FTPClient:
    def __init__(self,s):
        self.s = s
    def show(self):
        print("\n1) List file")
        print("2) Download file")
        print("3) Upload file")
        print("4) Quit")
        print("Enter a number to proceed.")

    def __list(self):
        self.s.send(b'L ')
        msg = self.s.recv(128).decode()
        if msg == 'OK':
            data = self.s.recv(4096)
            print(data.decode(),end="")
        else:
            print(msg)

    def __download(self):
        file_name = input("Enter the file name:")
        msg = "D " + file_name
        self.s.send(msg.encode())
        message = self.s.recv(1024)
        if message != b'OK':
            print(message.decode())
            return

        print("Downloading...")
        file = open(file_name,mode="wb")
        while True:
            data = self.s.recv(1024)
            if data == b'complete':
                break
            file.write(data)
        print("Successfully downloaded file '{}'".format(file_name))

    def __upload(self):
        file_name = input("Enter the file name:")
        try:
            file = open(file_name,"rb")
        except FileNotFoundError:
            print("No such file exists")
            return
        except Exception as e:
            print(e)
            return
        msg = "U " + file_name
        self.s.send(msg.encode())
        message = self.s.recv(1024)
        if message != b'OK':
            print(message.decode())
            return

        while True:
            data = file.read(1024)
            if not data:
                self.s.send(b'complete')
                print("Upload file '{}' successfully".format(file_name))
                break
            self.s.send(data)

    def __quit(self):
        self.s.send(b'Q ')
        self.s.close()
        sys.exit("Client logged out")



    def run(self):
        number = int(input(">>>"))
        if number == 1:
            self.__list()
        elif number == 2:
            self.__download()
        elif number == 3:
            self.__upload()
        elif number == 4:
            self.__quit()
        else:
            print("Unexpected number received")



def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.connect(ADDR)

    f = FTPClient(s)
    while True:
        f.show()
        f.run()

main()