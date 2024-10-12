n = int(input())
num = 0
s = 0
for _ in range(n):
    dic = eval(input()).values()
    # 下面这一步比较重要，这里我分解一下。
    # 输入{'a':{'b':10,'c':6}}后，dic为dict_values([{'b': 10, 'c': 6}])，注意此时是dict_values类。
    # 如果想要取出里面的字典需要先转换list，变成list[{'b': 10, 'c': 6}],{'b': 10, 'c': 6}为第一个元素。
    ans = list(dic)[0]
    # print(ans, type(ans))
    l = list(ans.values())
    num += len(l)
    s += sum(l)
print(f'{n} {num} {s}')

# 4
# {'a': {'b': 10, 'c': 6}}
# {'b': {'c': 2, 'd': 7}}
# {'c': {'d': 10}}
# {'d': {}}
