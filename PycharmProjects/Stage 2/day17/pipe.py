"""
pipe.py 管道通信
注意：
    1.　管道通信只能应用于一个父子进程中
    2. 管道对象在父进程中创建，子进程通过copy父进程代码获取管道
"""

from multiprocessing import Process,Pipe

"""
# 创建管道
fd1,fd2 = Pipe()

def app1():
    print("启动app1,请登录")
    print("请求app2　授权")
    fd1.send("app1 请求登录")   # 写入管道
    data = fd1.recv()
    if data == ("David",123):
        print("{}登录成功".format(data[0]))

def app2():
    data = fd2.recv()   #　阻塞等待读取管道内容
    print(data)
    fd2.send(('David',123))

p1 = Process(target=app1)
p2 = Process(target=app2)

p1.start()
p2.start()

p1.join()
p2.join()
"""

# 若为False,表示单向管道
# fd1只能读(即调用recv),fd2只能写(即调用send)
fd1,fd2 = Pipe(duplex=False)

def app1():
    print("启动app1,请登录")
    print("请求app2　授权")

    data = fd1.recv()
    if data == ("David",123):
        print("{}登录成功".format(data[0]))

def app2():
    fd2.send(('David',123))

p1 = Process(target=app1)
p2 = Process(target=app2)

p1.start()
p2.start()

p1.join()
p2.join()
