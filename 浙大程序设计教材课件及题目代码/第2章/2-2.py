# 本题目要求计算下列分段函数f(x)的值：
#
# 公式
#
# 输入格式:
# 输入在一行中给出实数x。
#
# 输出格式:
# 在一行中按“f(x) = result”的格式输出，其中x与result都保留一位小数。

InputNumber = float(input())
if InputNumber == 0:
    result = 0
else:
    result = 1 / InputNumber
print("f(%.1f) = %.1f" % (InputNumber, result))
