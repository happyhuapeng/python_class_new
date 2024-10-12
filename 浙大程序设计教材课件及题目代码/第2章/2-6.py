# 本题要求编写程序，计算交错序列 1-2/3+3/5-4/7+5/9-6/11+... 的前N项之和。
#
# 输入格式:
# 输入在一行中给出一个正整数N。
#
# 输出格式:
# 在一行中输出部分和的值，结果保留三位小数。

InputNumber = float(input())
result = 0
i = tmp = 1

while i <= InputNumber:
    if i % 2:
        result += i / tmp
    else:
        result -= i / tmp
    i += 1
    tmp += 2

print('%.3f' % result)
