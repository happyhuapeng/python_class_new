# 输入一个嵌套列表，再输入层数，求该层的数字元素个数。
#
# 输入格式:
# 第一行输入列表 第二行输入层数
#
# 输出格式:
# 在一行中输出元素个数

# 可能出错的样例
# [1,2,[1,2,[3]],[8,2]]
# 2

# st = eval(input())
# num = eval(input())
#
# def fct(st, deep, num):
#     s = 0
#     if isinstance(st, int) and deep == num:
#         s = 1
#     if isinstance(st, list):
#         deep += 1
#         for i in st:
#             s += fct(i, deep, num)
#     return s
#
#
# print(fct(st, 0, num))

# [1,2,[3,6,[5,6],[8]],8]
# 3

def f(deep, num, l=list()):
    cnt = 0
    for i in l:
        if isinstance(i, int) and deep == num:
            cnt += 1
        elif isinstance(i, (list, tuple)):
            cnt += f(deep+1, num, i)
    return cnt


l = eval(input())
n = int(input())
print(f'{f(1, n, l)}')
