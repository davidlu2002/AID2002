# s = open("student_info.txt","w")
# # a=1
# # s.write("student name:{}".format(a))
#
# info = (1, b'zs\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 18, 88.0)
# s.write("name:{}".format(info[1].decode()))

str01 = " 123 456"
str02 = str01.replace(" ", "")
print(str02)

print(b"\x00".decode())