# 一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。
#
# 本题要求编写程序，求一个给定的n阶方阵的鞍点。
#
# 输入格式： 输入第一行给出一个正整数n（1≤n≤6）。随后n行，每行给出n个整数，其间以空格分隔。
#
# 输出格式： 鞍点的个数

# 矩阵一行中可能有多个鞍点，比如矩阵
# 0 0
# 0 0
# 鞍点应该有四个，而我是按行的最大值去算鞍点，因此加的值应该是该值在该行个数

n = int(input())
l = []
count = 0
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    a = max(l[i])
    b = min(l[k][l[i].index(a)] for k in range(n))
    if b == a:
        count += l[i].count(a)
print(f'{count}')
