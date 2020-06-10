import getpass  # 输入隐藏
import hashlib  # 加密

# 输入隐藏
pwd = getpass.getpass("password:")
print(pwd)

# hash对象进行加密
hash = hashlib.md5("*#06l_".encode())
hash.update(pwd.encode())
pwd = hash.hexdigest()
print(pwd)
