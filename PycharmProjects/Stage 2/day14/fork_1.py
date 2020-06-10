# 运行fork.py文件，创建父进程

from time import sleep
import os

# 运行fork方法，创建子进程
pid = os.fork()
if pid < 0:
    print("Create process failed")

# 子进程执行部分
elif pid == 0:
    sleep(3)    # 假设子进程运行需要３秒
    print("The new process")

# 父进程执行部分
else:
    sleep(4)    #　假设父进程运行需要４秒
    print("The old process")
print("Fork test over")
# 提高代码运行效率