# 本题要求编写程序，输入10个字符，统计其中英文字母、空格或回车、数字字符和其他字符的个数。
#
# 输入格式:
# 输入为10个字符。最后一个回车表示输入结束，不算在内。
#
# 输出格式:
# 在一行内按照
#
# letter = 英文字母个数, blank = 空格或回车个数, digit = 数字字符个数, other = 其他字符个数
# 的格式输出。

import sys

s = sys.stdin.read()
letter, digit, blank, other = 0, 0, 0, 0
# s[:-1] 最后一个空格过滤掉 
for i in s[:-1]:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        blank += 1
    else:
        other += 1
print(f'letter = {letter}, blank = {blank}, digit = {digit}, other = {other}')

