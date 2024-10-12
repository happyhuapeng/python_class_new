# 给定M行N列的整数矩阵A，如果A的非边界元素A[i][j]大于相邻的上下左右4个元素，那么就称元素A[i][j]是矩阵的局部极大值。本题要求给定矩阵的全部局部极大值及其所在的位置。
#
# 输入格式：
# 输入在第一行中给出矩阵A的行数M和列数N（3≤M,N≤20）；最后M行，每行给出A在该行的N个元素的值。数字间以空格分隔。
#
# 输出格式：
# 每行按照“元素值 行号 列号”的格式输出一个局部极大值，其中行、列编号从1开始。要求按照行号递增输出；若同行有超过1个局部极大值，则该行按列号递增输出。若没有局部极大值，则输出“None 总行数 总列数”。

m, n = map(int, input().split())
l = []
flag = 0
for i in range(0, m):
    l.append(list(map(int, input().split())))
for i in range(1, m-1):
    for j in range(1, n-1):
        if l[i][j] > max([l[i-1][j], l[i+1][j], l[i][j-1], l[i][j+1]]):
            flag = 1
            print(f'{l[i][j]} {i+1} {j+1}')
if not flag:
    print(f'None {m} {n}')
