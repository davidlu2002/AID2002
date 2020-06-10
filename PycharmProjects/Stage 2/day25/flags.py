"""
    flags.py
    flags 扩展功能演示
"""

import re

s = """Hello
北京
"""

"""
# 1 只能匹配ASCII编码
regex = re.compile(r'\w+',flags=re.ASCII)
"""

"""
# 2 匹配时不区分大小写
regex = re.compile(r'[a-z]+',flags=re.IGNORECASE)
"""

"""
# 3 .可以匹配换行
regex = re.compile(r'.+',flags=re.DOTALL)
"""

"""
# 4 ^,$可以匹配每一行的开头/结尾位置
regex = re.compile(r'^北京',flags=re.MULTILINE)
"""

l = regex.findall(s)
print(l)