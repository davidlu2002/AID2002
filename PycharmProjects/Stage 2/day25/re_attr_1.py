"""
    re_attr_1.py    re模块　功能函数演示1
"""


import re

s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"    # 正则表达式

# re　模块调用findall
l = re.findall(pattern,s)
print(l)

# compile　对象调用findall
# pos,endpos代表所需寻找的区间
regex = re.compile(pattern)
l = regex.findall(s,3,5)
print(l)


# 切割字符串
l = re.split(r'[:,]',s)
print(l)

# 替换匹配到的字符串中的某些元素
s = re.sub(r':',"-",s)
print(s)