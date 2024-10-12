# 输入一个列表，去掉列表中重复的数字，按原来次序输出！
#
# 输入格式:
# 在一行中输入列表
#
# 输出格式:
# 在一行中输出不重复列表元素

l = eval(input())
print(*sorted(set(l), key=l.index), sep=' ')

