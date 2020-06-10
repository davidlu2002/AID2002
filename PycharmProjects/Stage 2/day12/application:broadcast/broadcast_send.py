"""
    广播发送
    １．创建ｕｄｐ套接字
    ２．设置可以发送广播
    ３．循环向广播地址发送
        广播地址：ifconfig -- broadcast
"""

from socket import *
from time import sleep

# 广播地址:终端ifconfig查找。是每个网络的最大地址
# 向广播地址发送，则网段内所有主机都能接收

broadcast_addr = ("192.168.18.255",10311)

s = socket(type=SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = "撒旦付付付付付付付付"

while True:
    sleep(2)
    s.sendto(data.encode(),broadcast_addr)

