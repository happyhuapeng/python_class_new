def list_app(old_list, new_list=list(),weight=list()):
    """#isinstance去判断遍历的l是不是还是一个list如果还是list,用递归继续反复遍历"""
    weight.append('0')
    for l in old_list:
        if isinstance(l, (tuple, list)):
            list_app(l)  # 调用递归
        else:
            # 如果不是,把l添加进一个新的list
            new_list.append(l*len(weight))
    weight.pop()
    return new_list


l = eval(input())
ans = list(filter(lambda x: isinstance(x, int), list_app(l)))
print(sum(ans))


# def f(l, cnt=1):
#     res = 0
#     for i in l:
#         if isinstance(i, int):
#             res += cnt * i
#         else:
#             res += f(i, cnt + 1)
#     return res
#
#
# print(f(eval(input())))
