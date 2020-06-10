from time import sleep
import os
print("=======================")
a = 1

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child process")
    print("a =",a)
    a = 10000

# 父进程执行部分
else:
    sleep(1)
    print("Parent process")
    print("a =",a)

print("All a ->",a)
print("Fork test over\n")
