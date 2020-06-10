from socket import *
import os,sys

sockfd = socket()
sockfd.bind(('0.0.0.0',10311))
sockfd.listen(5)


while True:


