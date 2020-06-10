import re
s = "2568899732@qq.com 1234567890 45% 1.45 1/3"

# 1 匹配一个.com邮箱格式字符串
result = re.findall(r'\w+@\w+.com',s)
print(result)

# 2 匹配一个密码　８－１２为数字字母下划线构成
result = re.findall(r'\w{8,12}',s)
print(result)

# 3 匹配任意一个数字
result = re.findall(r'-?\d+/?\.?\d*%?',s)
print(result)

# 4 匹配一段文字中以大写字母开头的单词
a = "AFS iPython3 Unveils Reports Showing U.S. Metalcasters Account for $44.3 Billion in Direct Economic Benefit May 19, 2020 The U.S. metalcasting industry accounts for $44.3 billion in direct economic benefit and a total national economic impact for the U.S. of $110.52 billion, according to a new study released today by the American Foundry Society."
result = re.findall(r'\b[A-Z]\S*-?\S*',a)
print(result)

print(re.search(r'(ab)+',"abababab").group())