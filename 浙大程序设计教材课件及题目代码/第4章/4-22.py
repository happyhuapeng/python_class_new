# 一个矩阵元素的“鞍点”是指该位置上的元素值在该行上最大、在该列上最小。
#
# 本题要求编写程序，求一个给定的n阶方阵的鞍点。
#
# 输入格式：
# 输入第一行给出一个正整数n（1≤n≤6）。随后n行，每行给出n个整数，其间以空格分隔。
#
# 输出格式：
# 输出在一行中按照“行下标 列下标”（下标从0开始）的格式输出鞍点的位置。如果鞍点不存在，则输出“NONE”。题目保证给出的矩阵至多存在一个鞍点。

def find_point(n_):
    for i in range(n_):
        for j in range(n_):
            if map_[i][j] == max(map_[i]) and map_[i][j] == min([map_[k][j] for k in range(n_)]):
                return i, j
    return ('NONE',)

n = int(input())
map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split())))
print(*find_point(n))


