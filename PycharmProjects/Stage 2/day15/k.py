
# a.pop('a')
# print(a)

# for i in a:
#     if a[i] == 2:
#         msg = '12345'
# print(msg)

# s = ['abc']
# print(" ".join(s))

"""
def fun01():
    return

def fun02():
    sys.exit()


import os,sys
pid = os.fork()
if pid == 0:
    fun01()
elif pid > 0:
    fun02()
"""


# for i in a:
#     if i == "a":
#         del a[i]
# print(a)

# for i in a.values():
#     if i == 1:
#         print("a")


# import time
#
# count1 = count2 = 0
# aw = 0
# while aw < 1000:
#     s_ = time.time()
#     for i in a:
#         if a[i] == 3:
#             print("ok")
#     e_ = time.time()
#     t1 = e_-s_
#
#     a_ = time.time()
#     for i in a.values():
#         if i == 3:
#             print("ok")
#     b_ = time.time()
#     t2 = b_-a_
#     if t2 / t1 > 1:
#         count1 += 1
#     elif t2 / t1 < 1:
#         count2 += 1
#     aw += 1
#
# print(count1)
# print(count2)

a = {'a':1,'b':2}

def connect(b):
    print(id(b))
    for b in a:
        print(id(b))
        if b == "a":
            print(id(b))

connect(110)

