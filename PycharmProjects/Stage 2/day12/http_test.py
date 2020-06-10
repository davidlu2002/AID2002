from socket import *
s = socket()
s.bind(("0.0.0.0",10312))
s.listen(5)
c,addr = s.accept()
print("Connected from",addr)
data = c.recv(4096)
print(data.decode())

c.close()
s.close()


