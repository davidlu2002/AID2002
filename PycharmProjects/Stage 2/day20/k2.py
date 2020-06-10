from socket import *
from threading import Thread
import os


s = socket()
s.connect(('0.0.0.0',10312))
data = input(">>>")
