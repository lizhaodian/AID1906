"""
regex.py    re模块    功能函数演示
"""

import re

# 目标字符串
s = 'Alex:1994,Sunny:1996'
# pattern = r'\w+:\d+'    # 正则表达式
# pattern = r'(\w+):\d+'
pattern = r'(\w+):(\d+)'

# re模块直接调用findall
l = re.findall(pattern, s)  # 返回列表,但是如果有子组,只能获取到子组对应的内容
print(l)    # ['Alex:1994', 'Sunny:1996']
            # 存在子组时,只返回子组匹配 ['Alex', 'Sunny']
            # 存在多个子组时,只返回子组匹配 [('Alex', '1994'), ('Sunny', '1996')]

# compile 对象调用findall
regex = re.compile(pattern)
# l = regex.findall(s)    # 只有用re模块调用的才有flags,这个regex没有flags,但是在使用compile可以写flags
l = regex.findall(s, 0, 12)  # 下标0到11位置字符串检测匹配 [('Alex', '1994')]
print(l)


# split()切割
# 按照正则表达式匹配内容介个字符串,返回列表
l = re.split(r'[:,]', s)    # 按照:,进行切割 ['Alex', '1994', 'Sunny', '1996']
print(l)


# sub()替换,返回替换后的字符串
s = re.sub(r':','-', s) # 使用-去替换正则表达式所匹配到的内容,返回替换后的字符串
print(s)    # Alex-1994,Sunny-1996


