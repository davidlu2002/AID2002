"""
    http_server v1.0
    需求：
    １．获取来自浏览器的请求
    ２．判断如果请求内容是/，就将index.html返回给客户端
    ３．如果请求的是其他内容，返回404
"""

from socket import *

# 客户端处理
def request(connfd):
    data = connfd.recv(4096) # 接受＋获得http请求
    # 防止浏览器异常退出
    if not data:
        return

    # 获取所需信息
    info_line = data.decode().split("\n")[0]
    info = info_line.split(" ")[1]

    if info == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Page not found<h1>"

    connfd.send(response.encode())

# 1 搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",10311))
sockfd.listen(3)
print("Waiting for connection...")

while True:
    connfd,addr = sockfd.accept()
    print("Connected from",addr)
    request(connfd) # 处理客户端请求
