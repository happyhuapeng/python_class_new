# 本题要求编写程序，读入5个字符串，按由小到大的顺序输出。
#
# 输入格式：
# 输入为由空格分隔的5个非空字符串，每个字符串不包括空格、制表符、换行符等空白字符，长度小于80。
#
# 输出格式：
# 按照以下格式输出排序后的结果：
#
# After sorted:
# 每行一个字符串

s = list(input().split())
s.sort()
print(f'After sorted:')
print(*s, sep='\n')
