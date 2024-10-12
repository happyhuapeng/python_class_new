# 读入2个正整数A和B，1<=A<=9, 1<=B<=10,产生数字AA...A,一共B个A
#
# 输入格式:
# 在一行中输入A和B。
#
# 输出格式:
# 在一行中输出整数AA...A,一共B个A

A, B = map(int, input().split(','))
result = i = 0

while i < B:
    result += A * 10 ** i
    i += 1

print(f'{result}')

