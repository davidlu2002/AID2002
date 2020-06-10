"""
    re模块　功能演示2
"""
import re

s = "今年是2019年,建国70周年"
pattern = r'\d+'

# 1 finditer: 返回迭代对象
it = re.finditer(pattern,s)
for i in it:
    print(i.group())    # .group()　获取match对象的内容


# 2 fullmatch: 完全匹配一个字符串(从开头到结尾),匹配不到则返回None
fm = re.fullmatch(r'[,\w]+',s)
print(fm.group())


# 3 match: 匹配某个字符串的开头位置
m = re.match(r'\w+',s)
print(m.group())


# 4 search: 匹配第一处符合正则表达式的字符
m = re.search(r'\d+',s)
print(m.group())





