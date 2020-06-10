from socket import *

s = socket()
s.bind(("0.0.0.0",10311))
s.listen(5)

c,addr = s.accept()
print("Connected from",addr)

data = c.recv(4096)
print(data)

response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Connection Received</h1>
"""

c.send(response.encode())
c.close()
s.close()


