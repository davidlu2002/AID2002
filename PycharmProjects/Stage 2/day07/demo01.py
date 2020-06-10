# 1 b转换：只能转换ascii码
s1 = "hello"    # 字符串
s2 = b"hello"   # 字节串（转成二进制形式）


# 2 若不是ascii码，用encode转换
# 看得懂 --> 看不懂
s3 = "你好".encode()
print(s3)


# 3 用decode把字节串转换回utf-8字符串
s4 = s3.decode()
print(s4)