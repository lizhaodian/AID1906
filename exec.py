"""
编写接口程序,从终端输入端口名称获取端口信息中的地址值

思路分析:
1. 根据输入的端口名称找到对应的段落
2. 在段落正则匹配address
"""

import re

def get_address(port):
    f = open('exc.txt')
    while True:
        # 获取一段内容
        data = ''
        for line in f:
            if line == '\n':
                break
            data += line

        # data为空说明到了文档结尾
        if not data:
            break

        # 判断是不是想要的段落
        obj = re.match(port,data)   # 匹配开始位置
        if obj:
            # 如果obj不为None就是目标段落
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r'(\d{1,3}\.){3}\d{1,3}/\d+|Unknow'
            obj = re.search(pattern,data)
            return obj.group()
    return '没有该端口'

if __name__ == '__main__':
    port = input('端口:')
    print(get_address(port))
