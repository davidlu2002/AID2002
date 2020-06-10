"""
    thread_server.py    基于线程thread的线程并发
"""

from socket import *
from threading import Thread
import os
import signal

HOST = '0.0.0.0'
PORT = 10311
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("PORT 10311 waiting for connection...")

def handle(c,addr):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            print("Connection from {} has broken.".format(addr))
            print("PORT 10311 waiting for connection...")
            os._exit(0)
        print(data.decode())
        c.send(b'OK\n')

while True:
    try:
        c,addr = s.accept()
        print("Connected from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    t = Thread(target=handle,args=(c,addr))
    t.start()