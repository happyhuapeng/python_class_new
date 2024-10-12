# def list_app(old_list):
#     """#isinstance去判断遍历的l是不是还是一个list如果还是list,用递归继续反复遍历"""
#     new_list = list()
#     for l in old_list:
#         if isinstance(l, (tuple, list)):
#             new_list.extend(list_app(l))  # 调用递归
#         else:
#             new_list.append(l)
#     return new_list


# def list_app(old_list, new_list=list()):
#     """#isinstance去判断遍历的l是不是还是一个list如果还是list,用递归继续反复遍历"""
#     for l in old_list:
#         if isinstance(l, (tuple, list)):
#             list_app(l)  # 调用递归
#         else:
#             # 如果不是,把l添加进一个新的list
#             new_list.append(l)
#     return new_list

# l = eval(input())
# ans = list(filter(lambda x: isinstance(x, int), list_app(l)))
# print(sum(ans))

