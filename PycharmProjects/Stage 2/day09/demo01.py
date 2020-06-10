"""
    文件的偏移量
        1.每次open打开文件，文件的偏移量默认在开头
        2.以a的方式打开文件，偏移量在末尾
"""
a = open("abc.txt", mode="rb+")
# a.write("new_info_".encode())

a.read(3)   # read也可以改变偏移量

print(a.tell()) # 查看文件的偏移量

# 写入新数据，可以根据偏移量在文件的任意位置写入
a.write("new02".encode())

a.close()