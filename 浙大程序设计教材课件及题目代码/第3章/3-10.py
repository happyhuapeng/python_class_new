# 英文辅音字母是除A、E、I、O、U以外的字母。本题要求编写程序，统计给定字符串中大写辅音字母的个数。
#
# 输入格式：
# 输入在一行中给出一个不超过80个字符、并以回车结束的字符串。
#
# 输出格式：
# 输出在一行中给出字符串中大写辅音字母的个数。

# import re
# s = input()
# fliter_s = re.sub(r'[B-DF-HJ-NP-TV-Z]', '', s)
# print(len(s)-len(fliter_s))

s = input()
ans = list(filter(lambda x: x.isupper() and x not in ('A', 'E', 'I', 'O', 'U'), s))
print(len(ans))
