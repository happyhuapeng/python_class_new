# 本题要求编写程序，从给定字符串中查找某指定的字符。
#
# 输入格式：
# 输入的第一行是一个待查找的字符。第二行是一个以回车结束的非空字符串（不超过80个字符）。
#
# 输出格式：
# 如果找到，在一行内按照格式“index = 下标”输出该字符在字符串中所对应的最大下标（下标从0开始）；否则输出"Not Found"。
a = input()
s = input()
pos = s.rfind(a)
print(f'index = {pos}') if pos != -1 else print(f'Not Found')
