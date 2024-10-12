# 求一个3*3二维数组中每行的最大值和每行的和。
#
# 输入格式:
# 在一行中输入9个小于100的整数，其间各以一个空格间隔
#
# 输出格式:
# 输出3行3列的二维数组，并在每行后面分别输出每行最大值和每行元素的和，每个数据输出占4列。

s = list(map(int, input().split()))
for i in range(0, 9, 3):
    su = 0
    max = s[i]
    for j in range(i, i+3):
        su = su+s[j]
        if s[j] > max:
            max = s[j]
        print("%4d"% s[j], end="")
    print("%4d%4d"% (max, su))
