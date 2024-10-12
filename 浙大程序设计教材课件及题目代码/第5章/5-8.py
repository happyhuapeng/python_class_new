# 求指定区间内能被3,5和7整除的数的个数
#
# 输入格式:
# 在一行中从键盘输入2个正整数a,b（1<=a<b<=10000000），用空格隔开。
#
# 输出格式:
# 在一行输出大于等于a且小于等于b的能被3,5和7整除的数的个数。

# a, b = map(int, input().split())
# cnt = 0
# for i in range(a, b+1):
#     if i % 105 == 0:
#         cnt += 1
# print(cnt)

a, b = map(int, input().split())
s = set(i for i in range(a, b + 1) if i % 105 == 0)
print(len(s))
