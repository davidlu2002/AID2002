"""
    套接字属性
"""
import socket
s = socket.socket()

print("地址类型：",s.family)
print("套接字类型：",s.type)
print("绑定地址：",s.getsockname())
print("文件描述符：",s.fileno()) #　０，１，２被系统占用
