# 给定两个均不超过9的正整数a和n，要求编写程序求a+aa+aaa++⋯+aa⋯a（n个a）之和。
#
# 输入格式：
# 输入在一行中给出不超过9的正整数a和n。
#
# 输出格式：
# 在一行中按照“s = 对应的和”的格式输出。

a, n = map(int, input().split())
result = tmp = 0
i = j = 1

while i <= n:
    tmp = 0
    j = 1
    while j <= i:
        tmp += a * 10 ** (j-1)
        j += 1
    result += tmp
    i += 1

print(f's = {result}')
