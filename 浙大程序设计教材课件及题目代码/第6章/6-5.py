# 输入一个嵌套列表，嵌套层次不限，根据层次，求列表元素的加权个数和。第一层每个元素算一个元素，第二层每个元素算2个元素，第三层每个元素算3个元素，第四层每个元素算4个元素,...,以此类推！
#
# 输入格式:
# 在一行中输入一个列表。
#
# 输出格式:
# 在一行中输出加权元素个数值。

def list_f(l=list(), cnt=1):
    res = 0
    for i in l:
        if isinstance(i, int):
            res += 1 * cnt
        else:
            res += list_f(i, cnt + 1)
    return res


print(list_f(eval(input())))
