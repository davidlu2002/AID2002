from socket import *
from select import *

# 功能实现
class HTTPServer:
    def __init__(self,addr,dir):
        self.addr = addr
        self.dir = dir
        self.__create_socket()

    # 创建套接字
    def __create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.addr)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("PORT {} is listening...".format(self.addr[1]))
        # IO多路复用接收客户端请求
        self.__handle()

    def __handle(self):
        self.rlist = [self.sockfd]
        self.wlist = self.xlist = []
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c,addr = r.accept()
                    print("Connected from",addr)
                    self.rlist.append(c)
                else:
                    self.__request(r)

    def __request(self,connfd):
        request = connfd.recv(4096)
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容(将字节串按行分割)
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(), ":", info)
        if info == "/" or info[-5:] == ".html":
            self.__get_html(info,connfd)
        else:
            self.__get_data(connfd)

    # 返回网页
    def __get_html(self,info,connfd):
        if info == "/":
            path = self.dir + "/index.html"
        else:
            path = self.dir + info
        try:
            file = open(path)
        except Exception:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Page Not Found</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += file.read()
        finally:
            connfd.send(response.encode())

    # 其他数据（如图片等）
    def __get_data(self,connfd):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting for response</h1>"
        connfd.send(response.encode())

# 用户使用
if __name__ == '__main__':
    """
    可以通过HTTPServer类快速搭建服务，展示自己的网页
    """
    # 用户决定的参数
    HOST = '0.0.0.0'
    PORT = 10311
    ADDR = (HOST,PORT)
    DIR = './static' # 网页存储位置

    httpd = HTTPServer(ADDR,DIR)
    httpd.serve_forever() # 启动服务

