# 给定公司N名员工的工龄，要求按工龄增序输出每个工龄段有多少员工。
#
# 输入格式:
# 输入首先给出正整数N（≤10^5），即员工总人数；随后给出N个整数，即每个员工的工龄，范围在[0, 50]。
#
# 输出格式:
# 按工龄的递增顺序输出每个工龄的员工个数，格式为：“工龄:人数”。每项占一行。如果人数为0则不输出该项。

from collections import Counter
n = int(input())
l = list(map(int, input().split()))
l = Counter(l).most_common(n)
l.sort()
for i in range(len(l)):
    print(f'{l[i][0]}:{l[i][1]}')
