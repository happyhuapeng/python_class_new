# 输入一个正整数m(20<=m<=100)，计算 11+12+13+...+m 的值。
#
# 输入格式:
# 在一行输入一个正整数m。
#
# 输出格式:
# 在一行中按照格式“sum = S”输出对应的和S.

number = int(input())
i = 11
sum = 0

while i <= number:
    sum += i
    i += 1

print(f'sum = {sum}')