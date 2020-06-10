"""
queue_0.py  队列通信
注意：消息队列先进先出
"""

from multiprocessing import Queue,Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(4)    # 最大长度为4

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)
    q.put(randint(1,16))

def request():
    print("开始摇号")
    while True:
        sleep(2)
        try:
            print(q.get(timeout=3))
        except:
            break

p1 = Process(target=handle)
p2 = Process(target=request)

p1.start()
p2.start()

p1.join()
p2.join()