"""
    读文件操作
"""

"""
# 一、读文本信息
# 1 打开文件
a = open("abc", mode="r")

# 2 读取文件中的数据
data = a.read()
print(data)

# 3 关闭文件
a.close()
"""

"""
# 二、读图片信息(要用字节串的格式读取)
# 1 打开文件(rb:字节串格式)
b = open("def.jpg", mode="rb")

# 2 读取文件中的数据
data = b.read()
print(data)

# 3 关闭
b.close()
"""

"""
# 三、按指定字符/字节读取文件
# 1 打开文件
c = open("abc", mode="r")

# 2 读取文件中的数据
while True:
    data = c.read(11)
    print(data)
    if data == "":
        break

# 3 关闭
c.close()
"""

"""
# 四、readline
# 1 打开文件
d = open("abc", mode="r")

# 2 使用readline方法读取文件
# (1) 不加参数，默认每次读一行
# while True:
#     data = d.readline()
#     print(data, end="")

# (2) 加参数，赋值这一行的前n个字符
data = d.readline(5)
print(data)

# 3 关闭
d.close()
"""

"""
# 五、readlines
# 将文件内容整合成列表并打印
# 1 打开文件
e = open('abc',mode="r")

# 2 读取数据
# 不加参数，列表包含文件内所有元素
# data = e.readlines()
# print(data)

# 加参数，与readline用法类似
data = e.readlines(101)
for i in data:
    print(i,end="")
    print(len(i))

# 3 关闭
e.close()
"""

""""""
# 六
# 1 打开文件
f = open("abc", mode="r")
for i in f:
    print(i, end="")

# 4 关闭
f.close()