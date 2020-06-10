"""
    信号处理僵尸
"""
import os,sys,signal

# 子进程退出时父进程忽略退出行为，信号将子进程关闭（所有僵尸子进程）
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Get child PID:",os.getpid())
    sys.exit("Child process exit")
else:
    pid,status = os.wait()
    print("Child PID:",pid)
    print("Child process status:",status)

    while True: # 父进程不退出
        pass
