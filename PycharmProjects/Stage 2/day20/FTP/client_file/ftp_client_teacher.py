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
        print("1) List file")
        print("2) Download file")
        print("3) Upload file")
        print("4) Quit")
        print("Enter a number to proceed.")

    def __list(self):
        self.s.send(b'L ')
        msg = self.s.recv(128).decode()
        if msg == 'OK':
            data = self.s.recv(4096)
            print(data.decode())
        else:
            print(msg)

    def __download(self):
        while True:
            file_name = input("Enter the file name (enter esc to exit):")
            if file_name == "esc":
                break
            msg = "D " + file_name
            self.s.send(msg.encode())
            message = self.s.recv(1024)
            if message == "None":
                print("No such file exists")
                continue
            print("Downloading...")

            file = open(file_name,mode="wb")
            while True:
                data = self.s.recv(1024)
                print(data)
                if not data:
                    break
                file.write(data)
            print("Successfully downloaded file '{}'".format(file_name))

    def __upload(self):
        pass
    def __quit(self):
        self.s.send(b'Q ')
        sys.exit("Thanks for using our service")

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
            raise ValueError("Unexpected number received")



def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    f = FTPClient(s)
    while True:
        f.show()
        f.run()

main()