# 本题要求编写程序，找出给定的n个数中的最大值及其对应的最小下标（下标从0开始）。
#
# 输入格式:
# 输入在第一行中给出一个正整数n（1<n≤10）。第二行输入n个整数，用空格分开。
#
# 输出格式:
# 在一行中输出最大值及最大值的最小下标，中间用一个空格分开。

n = int(input())
l = list(map(int, input().split()))
print(f'{max(l)} {l.index(max(l))}')