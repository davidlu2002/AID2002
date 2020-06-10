"""
    正则表达式１
"""

import re

s = "asdjkewfjksadjfkasd12302109312dsafewacplonrtkpgt"

# 1 或
result = re.findall('a|p|f',s)
print(result)

# 2 .表示任意单个字符(换行符除外)
result = re.findall('a.d',s)
print(result)

# 3 字符集
# 表示匹配字符集中的任意一个字符
result = re.findall('[aeiou]',s)
print(result)
# or:
result = re.findall('[0-9]',s)
print(result)
# or:集合组合
result = re.findall('[f0-9a-i]',s)
print(result)

# 4 ^: ^在字符集内，匹配除字符集之外的字符
result = re.findall('[^0-8a-z]',s)
print(result)
print("===========================")
# ^: ^接一个字符，表达所需查找的字符串的开头位置
result = re.findall('^asd',s)
print(result)

# 5 $: 所需查找的字符串的结尾位置
result = re.findall('pgt$',s)
print(result)

# 6 *: 匹配*前面的一个字符出现0次或多次
# 单个字符
result = re.findall('wo*',"woooooooo~w!wo~")
print(result)
# 字符串 e.g:查找大写字母开头的字符
result = re.findall('[A-Z][a-z]*',"How are you, Jame?")
print(result)

# 7 +:匹配+前面的一个字符出现1次或多次
result = re.findall('[A-Z][a-z]+',"I am going to Disneyland")
print(result)   # I不会被匹配到

# 8 ?:匹配?前面的一个字符出现0次或1次
# e.g: 匹配下列所有数字（负数＋正数）
result = re.findall('-?[0-9]*',"123 -4 55 -120")
print(result)

result = re.findall('[^ ]+',"Port-9 Error #404# %@STD")
print(result)

# 9 {n}/{m,n}:匹配前面的字符出现n/m-n次
# e.g1:
result = re.findall('ab{3}',"abbbbbbasdwfabasdfwev")
print(result)
# e.g2:
result = re.findall('1[0-9]{10}',"张三:17526914076")
print(result)
# e.g3:
result = re.findall('a.{3}',s)
print(result)
# e.g4:
result = re.findall('ab{2,4}',"abbabasdfabbbasfdbbabbbbb")
print(result)

# 10 \d or \D:匹配任意数字/非数字字符
# e.g1:
result = re.findall('\d{1,5}',"1203,10311")
print(result)
# e.g2:
result = re.findall('\D{3,10}',s)
print(result)

# 11 \w or \W:匹配任意普通字符/非普通字符
# 普通字符：数字、字母、下划线、普通UTF-8字符
# e.g1:
result = re.findall('\w+',"server_port = 安保处的")
print(result)
# e.g2:
result = re.findall('\W+',"server_port = 安保处的")
print(result)

# 12 \s or \S:匹配任意的空字符或非空字符
# 空字符：空格,\r,\n,\t,etc.
result = re.findall('\w+\s+\w+',"Hello    world")
print(result)

# 13 \A == ^; \Z == $

# 14 \b or \B:匹配单词边界或非单词边界
#　单词边界：数字、字母（汉字）、下划线与其他字符的边界处
result = re.findall(r'\bis\b',"This is a test.")
print(result)


# 15 转义：在所需字符前加\可清除其原来表达的内容，来表达它本身的含义
# e.g1:
result = re.findall('\*\*',"a*b**")
print(result)
# e.g2:匹配所有数字
result = re.findall('-?\d+\.?\d*',"1.1 -3.8 38 110.5")
print(result)
# e.g3:初始化\b(\b表示退格)
result = re.findall('\\bis\\b',"This is a test.")
print(result)

# 16 r:正则字符串前加r，表示原生字符串(不转义)
result = re.findall(r'\bis\b',"This is a test.")
print(result)
print("==================================")

# 贪婪/非贪婪模式
result = re.findall(r'\[.+?\]',"[a],[b],[cd]")
print(result)
