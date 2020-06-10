"""
    实现逆波兰表达式
"""
from sstack import *

st = Sstack()
while True:
    exp = input()
    tmp = exp.split()
    for i in tmp:
        if i not in ["+","-","*","/","p"]:
            st.push(float(i))
        elif i == "+":
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == "-":
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == "*":
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == "/":
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == "p":
            print(st.top())

