a = open("demo04.py", mode="w")
a.write("def say_hello():\n")
a.write("   print('Hello')\n")
a.write("say_hello()")
a.close()

b = open("demo04.py", mode="r")
data = b.readlines()
for i in data:
    print(i, end="")
