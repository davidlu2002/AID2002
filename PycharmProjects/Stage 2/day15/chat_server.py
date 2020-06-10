"""
    chat room
    env: python3.6
    socket udp & fork
"""

from socket import *
import os,sys

"""
全局变量：很多封装模块都用或者有一定的含义
"""

# 用户信息　{name:address}
user = {}

# 服务器地址
ADDR = ("0.0.0.0",8888)

def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto('该用户存在'.encode(),addr)
        return

    # 通知其他人
    msg = "\n欢迎'{}'进入聊天室".format(name)
    for addr_ in user.values():
        s.sendto(msg.encode(),addr_)
    user[name] = addr
    s.sendto(b'OK', addr)

def do_chat(s,msg):
    for addr in user.values():
        s.sendto(msg.encode(),addr)

def do_logout(s,name):
    msg = "\n" + name + "已退出聊天室"
    for i in user:
        if i == name:
            s.sendto(b'EXIT', user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name]

# 处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        msg = data.decode().split(' ')
        # 根据不同的请求类型执行不同的函数
        # L 进入     C 聊天    Q　退出
        if msg[0] == 'L':
            do_login(s,msg[1],addr)
        elif msg[0] == 'C':
            msg[1] += ":"
            text = ' '.join(msg[1:])
            do_chat(s,text)
        elif msg[0] == 'Q':
            do_logout(s,msg[1])
# 搭建网络
def main():
    # udp套接字
    s = socket(type=SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid == 0:    # 父进程处理管理员消息
        while True:
            msg = input("管理员消息：")
            msg = "C " + "\n管理员消息：" + msg
            s.sendto(msg.encode(),ADDR)
    elif pid > 0:   # 子进程处理请求函数
        do_request(s)

main()

