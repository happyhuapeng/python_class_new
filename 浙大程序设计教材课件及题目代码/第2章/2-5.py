# 第2章-5 求奇数分之一序列前N项和 (15 分)
# 本题要求编写程序，计算序列 1 + 1/3 + 1/5 + ... 的前N项之和。
#
# 输入格式:
# 输入在一行中给出一个正整数N。
#
# 输出格式:
# 在一行中按照“sum = S”的格式输出部分和的值S，精确到小数点后6位。题目保证计算结果不超过双精度范围。

InputNumber = float(input())
tmp = 1
i = result = 0

while i < InputNumber:
    result += 1.0 / tmp
    tmp += 2
    i += 1

print('sum = %.6f' % result)
