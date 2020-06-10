"""
    给定一个顺序，判断出栈顺序是否正确
"""
from sstack import *
st = Sstack()

def istrue_poporder(push_order, pop_order):
    for item in push_order:
        st.push(item)
        while len(pop_order) != 0 and pop_order[0] == st.top():
            st.pop()
            pop_order.pop(0)

    return len(pop_order) == 0

print(istrue_poporder([1,2,3,4,5], [4,5,3,2,1]))
