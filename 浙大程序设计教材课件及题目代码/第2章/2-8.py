# 输入一个整数a和进制b，转换成十进制输出
#
# 输入格式:
# 在一行输入整数和进制
#
# 输出格式:
# 在一行十进制输出结果

a, b = map(int, input().split(','))
result = tmp = i = 0
while 1:
    result += (a % 10) * b ** i
    a //= 10
    i += 1
    if a == 0:
        break
print(f'{result}')

