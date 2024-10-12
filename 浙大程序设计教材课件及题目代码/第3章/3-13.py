# 本题要求编写程序，将给定字符串中的大写英文字母按以下对应规则替换：
#
# 原字母	对应字母
# A	Z
# B	Y
# C	X
# D	W
# …	…
# X	C
# Y	B
# Z	A
# 输入格式：
# 输入在一行中给出一个不超过80个字符、并以回车结束的字符串。
#
# 输出格式：
# 输出在一行中给出替换完成后的字符串。

s1 = [chr(i+65) for i in range(26)]
s2 = reversed(s1)
d1 = dict(zip(s1, s2))
s = input()
ans = map(lambda x: d1[x] if x.isupper() else x, s)
print(*ans, sep='')
