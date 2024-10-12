# 四则运算（用字典实现），比较c语言的switch语句。
#
# 输入格式:
# 在一行中输入一个数字 在一行中输入一个四帜运算符(+,-,*,/) 在一行中输入一个数字
#
# 输出格式:
# 在一行中输出运算结果（小数保留2位）

res = {'+': 'x+y', '-': 'x-y', '*': 'x*y', '/': "x/y if y!=0  else 'divided by zero'"}
# 除法部分分三元式表示
x = int(input())
operation = input()
y = int(input())
r = eval(res[operation])
if type(r) != str:
    print(format(r, '.2f'))
else:
    print(r)
