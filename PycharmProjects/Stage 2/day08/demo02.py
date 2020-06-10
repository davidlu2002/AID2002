"""
    文件写操作
"""

"""
# 一、写文本
# 1 打开文件
a = open("123", mode="w")

# 2 写入数据
a.write("呵呵哈哈呵呵哈哈哈\n")
a.write("阿斯蒂芬")

# 3 关闭
a.close()
"""

"""
# 二、写字节码
# 1 打开文件
b = open("123", mode="wb")

# 2 写入数据
b.write("呵呵哈哈呵呵哈哈哈\n".encode())
b.write("案的说法".encode())

# 3 关闭
b.close()
"""

"""
# 三、writelines
# 将列表写入文件

# 1 打开文件
c = open("123", mode="w")

# 2 写入数据
list01 = ["阿斯蒂芬洒洒地方\n", "爱上对方的分散"]
c.writelines(list01)

# 3 关闭
c.close()
"""

"""
# 四、追加写操作
# 1 打开文件
d = open("123", mode="a") # a: 追加写入

# 2 写入数据
d.write("追加写入01\n")
d.write("追加写入02\n")

# 3 关闭
d.close()
"""

"""
# 五、创建空文件
# 如果以写的方式打开一个不存在的文件会创建一个该文件
e = open("demo03.py", "w")
e.close()
"""