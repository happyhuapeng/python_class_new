# 在同一行依次输入三个值a,b,c，用空格分开，输出 b*b-4*a*c的值
#
# 输入格式:
# 在一行中输入三个数。
#
# 输出格式:
# 在一行中输出公式值。

# map函数 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
# input.split() 输入去除空格，如果是逗号则改为input.split(',')
a, b, c = map(int, input().split(','))
print(f'{b * b - 4 * a * c}')
