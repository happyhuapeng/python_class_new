# 给定一个n×n的方阵，本题要求计算该矩阵除副对角线、最后一列和最后一行以外的所有元素之和。副对角线为从矩阵的右上角至左下角的连线。
#
# 输入格式:
# 输入第一行给出正整数n（1<n≤10）；随后n行，每行给出n个整数，其间以空格分隔。
#
# 输出格式:
# 在一行中给出该矩阵除副对角线、最后一列和最后一行以外的所有元素之和。

n = int(input())
l, tmp = list(), list()
for _ in range(n):
    l.append(list(map(int, input().split())))
del l[n - 1]
for i in range(n - 1):
    del l[i][n - 1]
for i in range(1, n - 1):
    del l[i][n - i - 1]
for i in range(n - 1):
    tmp.extend(l[i])
print(sum(tmp))

# n = int(input())
# l = []
# for _ in range(n):
#     line = list(map(int, input().split()))
#     l.append(line)
# ans = 0
# for j in range(n):
#     for k in range(n):
#         if j != n - 1 and k != n - 1 and j + k != n - 1:
#             ans += l[j][k]
# print(ans)
