"""
    分组
"""

import re

# 加括号分组
# result = re.search(r'(王|李)\w{1,3}',"王者荣耀").group()
# print(result)

result = re.findall(r"(zs)+","zszszszszszszszszszszszszszszs")
print(result)

