"""
    模拟僵尸进程的产生
"""

import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Get child PID:",os.getpid())
    sys.exit("Child process exit")
else:
    """
    os.wait() 处理僵尸进程
    """
    pid,status = os.wait()
    print("Child PID:",pid)
    print("Child process status:",status)

    while True: # 父进程不退出
        pass

