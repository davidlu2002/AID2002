"""
    chat room 客户端
    发送请求，展示结果
"""

from socket import *
import os,sys

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 进入聊天室
def login(s):
    while True:
        name = input("请输入姓名：")
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            return name
        else:
            print(data.decode())

# 聊天



def send_msg(s,name):
    while True:
        try:
            msg = input(">>>")
        except KeyboardInterrupt:
            msg = "EXIT"
        if msg.strip() == "EXIT":
            data = "Q " + name
            s.sendto(data.encode(), ADDR)
            sys.exit("您已退出聊天室")
        data = 'C ' + name + " " + msg
        s.sendto(data.encode(),ADDR)

def recv_msg(s):
    while True:
        try:
            data,addr = s.recvfrom(1024)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == "EXIT":
            sys.exit()
        else:
            print(data.decode() + "\n>>>",end="")


# 搭建网络
def main():
    s = socket(type=SOCK_DGRAM)

    # 进入聊天室
    name = login(s)

    # 聊天
    pid = os.fork()
    if pid < 0:
        print("Error!")
        return
    elif pid == 0:
        recv_msg(s)  # 子进程负责消息接受
    else:
        send_msg(s, name)  # 父进程负责消息发送


main()