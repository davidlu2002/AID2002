"""
    re模块　功能演示3
    match对象属性演示
"""

import re
pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search("abcdefghi")

# match对象的属性
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos)   # 目标字符串结束位置
print(obj.re)   # 正则表达式
print(obj.string)   #　目标字符串
print(obj.lastgroup)    # 最后一组的组名
print(obj.lastindex)    # 最后一组的索引(即几个子组)
print("===============================")

# 属性方法
print(obj.span())   #　匹配到的字符串在字符串的起止位置
print(obj.start())  #　匹配到的字符串在字符串的开始位置
print(obj.end())    #　匹配到的字符串在字符串的结束位置

print(obj.groupdict())  # 捕获组的字典
print(obj.groups()) #　子组对应内容的元组
print("===============================")

print(obj.group())
print(obj.group(1)) #　获取第一个子组的内容
print(obj.group('pig')) # 获取名称为pig的子组的内容

