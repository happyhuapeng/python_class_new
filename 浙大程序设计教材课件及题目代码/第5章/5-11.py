# 输入用字符串表示两个字典，输出合并后的字典。字典的键用一个字母或数字表示。注意：1和‘1’是不同的关键字！
#
# 输入格式:
# 在第一行中输入第一个字典字符串；
#
# 在第二行中输入第二个字典字符串。
#
# 输出格式:
# 在一行中输出合并的字典，输出按字典序。
#
# "1" 的 ASCII 码为 49，大于 1，排序时 1 在前，"1" 在后。其它的字符同理。

# from collections import Counter

l = []
for _ in range(2):
    l.append(eval(input()))

# 把两个字典中相同的加在一起
# m, n = Counter(l[0]), Counter(l[1])
# x = dict(m + n)

# m字典存放int类型key，n字典存放字符类型。
m, n = dict(), dict()
for i in l:
    for j in i.keys():
        if isinstance(j, str):
            n[j] = n.get(j, 0) + i[j]
        else:
            m[j] = m.get(j, 0)+i[j]
m = dict(sorted(zip(m.keys(), m.values())))
m.update(dict(sorted(zip(n.keys(), n.values()))))
s = str(m)
s = s.replace(' ', '')
s = s.replace("'", '"')
print(s)

